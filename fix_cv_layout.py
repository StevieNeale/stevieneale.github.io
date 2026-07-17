from pathlib import Path

path = Path('CV.html')
text = path.read_text(encoding='utf-8')

css_start = text.find('.edu-logos img { height: 50px; width: auto; opacity: 0.8; }')
css_end = text.find('</style>', css_start)
if css_start == -1 or css_end == -1:
    raise SystemExit('Could not locate CSS block')

new_css = '''.edu-logos img { height: 50px; width: auto; opacity: 0.8; }

.cv-two-column {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 42px;
    align-items: start;
}
.edu-column, .cert-column {
    margin-bottom: 0;
}
.cert-column h3 {
    margin-bottom: 14px;
}
.cert-entry {
    margin-bottom: 26px;
}
.cert-entry .degree {
    margin-bottom: 4px;
}
@media screen and (max-width: 900px) {
    .cv-two-column {
        grid-template-columns: 1fr;
    }
}

.highlight-band {
    background-color: #d2e6e5;
    border-left: 5px solid #2cbdb5;
    padding: 10px 16px;
    margin-bottom: 16px;
    border-radius: 2px;
}
.highlight-band p { margin: 0; }
'''

# Insert new CSS before the closing </style>
stub = text[css_start:css_end]
replace_start = css_start
replace_end = css_end
before = text[:replace_start]
after = text[replace_end:]

# Replace only the old CSS subset from .edu-logos img through just before </style>
common_prefix = '.edu-logos img { height: 50px; width: auto; opacity: 0.8; }'
prefix_index = stub.find(common_prefix)
if prefix_index == -1:
    raise SystemExit('Unexpected CSS block structure')

new_text = before + new_css + after

# Replace the Education section using markers
edu_start = new_text.find('<hr class="section-divider">')
edu_end = new_text.find('<!-- ======================== INFORMATION TECHNOLOGY WORK EXPERIENCE ======================== -->', edu_start)
if edu_start == -1 or edu_end == -1:
    raise SystemExit('Could not locate Education section markers')

inside = new_text[edu_start:edu_end]

new_edu = '''<hr class="section-divider">

			<div class="cv-two-column">
				<div class="edu-column">
					<div class="edu-entry">
						<h3>Colorado Technical University</h3>
						<p class="degree">Master of Science</p>
						<p class="meta">Computer Science &nbsp;&bull;&nbsp; Graduated 2021</p>
						<p class="gpa">GPA 3.98</p>
						<p class="coursework"><strong>Coursework:</strong> Modern Operating Systems &bull; Computer Networking &bull; Design and Analysis of Algorithms &bull; Computer Systems Security Foundations &bull; Database Systems &bull; Systems Engineering Methods &bull; Digital Forensics &bull; Data Management &bull; Software Design &bull; Network Security &bull; Real-Time Systems</p>
					</div>

					<div class="edu-entry">
						<h3>Eastern University</h3>
						<p class="degree">Master of Arts</p>
						<p class="meta">Urban Studies Community Arts &nbsp;&bull;&nbsp; Graduated 2013</p>
						<p class="gpa">GPA 3.88</p>
					</div>

					<div class="edu-entry">
						<h3>University of West Florida</h3>
						<p class="degree">Bachelor of Fine Arts</p>
						<p class="meta">Musical Theatre &amp; Political Science Pre-Law &nbsp;&bull;&nbsp; Graduated 2009</p>
						<p class="gpa">GPA 3.85</p>
					</div>

					<div class="edu-entry">
						<h3>Coral Springs Christian Academy</h3>
						<p class="degree">High School Diploma</p>
						<p class="meta">National Honors Society &nbsp;&bull;&nbsp; Graduated 2004</p>
						<p class="gpa">GPA 4.0</p>
					</div>
				</div>

				<div class="cert-column">
					<h3>Certifications</h3>
					<div class="cert-entry">
						<p class="degree">Okta Certified Professional</p>
						<p class="meta">May 2026</p>
					</div>
					<div class="cert-entry">
						<p class="degree">Scrum Master Bootcamp</p>
						<p class="meta">Myriad Genetics &nbsp;&bull;&nbsp; November 2024</p>
					</div>
					<div class="cert-entry">
						<p class="degree">Microsoft Azure AZ-900</p>
						<p class="meta">June 2024</p>
					</div>
					<div class="cert-entry">
						<p class="degree">Google Cloud Digital Leader</p>
						<p class="meta">December 2022</p>
					</div>
					<div class="cert-entry">
						<p class="degree">Google IT Support</p>
						<p class="meta">July 2022</p>
					</div>
				</div>
			</div>

''' 

new_text = new_text[:edu_start] + new_edu + new_text[edu_end:]
path.write_text(new_text, encoding='utf-8')
print('updated')
