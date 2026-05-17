import re

with open('register.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Phone SVG icon (shared)
phone_svg = '<svg fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'

descriptions = {
    'nbmdc': (
        '<p style="margin-bottom: 0.5rem; border-left: 2px solid var(--color-border); padding-left: 1rem;">'
        'The <strong>National Building Mockup Design Competition (NBMDC)</strong> is one of the competition events '
        'held by the Civil Engineering Festival 2026 (Civfest 2026), specifically open to Senior High School (SMA/SMK) '
        'students and equivalents. It serves as a platform for participants to develop and express their ideas and '
        'creativity in constructing a small-scale house model that showcases Architectural Design, with a strong '
        'emphasis on Green Building innovation as a response to the challenges of the future.</p>\n'
        '<p style="margin-bottom: 2rem; border-left: 2px solid var(--color-border); padding-left: 1rem; padding-top: 0.5rem;">'
        'Theme: <em>\u201cGreen Building Design for Comfortable Future\u201d</em></p>'
    ),
    'nptc': (
        '<p style="margin-bottom: 0.5rem; border-left: 2px solid var(--color-border); padding-left: 1rem;">'
        'The <strong>National Project Tender Competition (NPTC)</strong> is a national-scale competition open to active '
        'undergraduate students in Civil Engineering programs across Indonesia. The competition challenges participants '
        'to demonstrate their creativity and innovation in developing efficient construction project tender strategies, '
        'with a focus on cost-effectiveness, time management, and quality assurance.</p>\n'
        '<p style="margin-bottom: 2rem; border-left: 2px solid var(--color-border); padding-left: 1rem; padding-top: 0.5rem;">'
        'Theme: <em>&ldquo;Smart Construction Management to Create Efficient and Green Infrastructure&rdquo;</em></p>'
    ),
    'nbdc': (
        '<p style="margin-bottom: 0.5rem; border-left: 2px solid var(--color-border); padding-left: 1rem;">'
        'The <strong>National Bridge Design Competition (NBDC)</strong> is a competition that serves as a platform for '
        'Civil Engineering students to develop their creativity, innovation, and inspiration in designing bridge '
        'structures. This year, the competition is integrated with the Green Building concept, encouraging participants '
        'to incorporate sustainable principles into their bridge design solutions.</p>\n'
        '<p style="margin-bottom: 2rem; border-left: 2px solid var(--color-border); padding-left: 1rem; padding-top: 0.5rem;">'
        'Theme: <em>\u201cTransforming the Future Through Sustainable Green Infrastructure Innovation\u201d</em></p>'
    ),
    'ncc': (
        '<p style="margin-bottom: 0.5rem; border-left: 2px solid var(--color-border); padding-left: 1rem;">'
        'The <strong>National Concrete Competition (NCC)</strong> is a competition that provides Civil Engineering '
        'students with a platform to develop their creativity, innovation, and efficiency in designing high-strength '
        'concrete mixtures. Participants are challenged to enhance the mechanical properties of concrete by '
        'incorporating recycled materials into the mix design.</p>\n'
        '<p style="margin-bottom: 2rem; border-left: 2px solid var(--color-border); padding-left: 1rem; padding-top: 0.5rem;">'
        'Theme: <em>&ldquo;Exploration of Recycled Alternative Materials as Concrete Components&rdquo;</em></p>'
    ),
    'nbc': (
        '<p style="margin-bottom: 0.5rem; border-left: 2px solid var(--color-border); padding-left: 1rem;">'
        'The <strong>National BIM Competition (NBC)</strong> is a national-scale competition open to active '
        'undergraduate students in Civil Engineering programs across Indonesia. It serves as a platform for '
        'participants to channel their creativity and innovation in designing building structures using Building '
        'Information Modeling (BIM) technology.</p>\n'
        '<p style="margin-bottom: 2rem; border-left: 2px solid var(--color-border); padding-left: 1rem; padding-top: 0.5rem;">'
        'Theme: <em>&ldquo;Green Building Design through BIM for a Sustainable Future&rdquo;</em></p>'
    ),
}

old_descriptions = {
    'nbmdc': r'<p[^>]*>NBMDC Civil Engineering Festival 2026[^<]*<em>[^<]*<\/em>\.<\/p>',
    'nptc':  r'<p[^>]*>NPTC Civil Engineering Festival 2026[^<]*<em>[^<]*<\/em>\.<\/p>',
    'nbdc':  r'<p[^>]*>NBDC Civil Engineering Festival 2026[^<]*<em>[^<]*<\/em>\.<\/p>',
    'ncc':   r'<p[^>]*>NCC Civil Engineering Festival 2026[^<]*<em>[^<]*<\/em>\.<\/p>',
    'nbc':   r'<p[^>]*>NBC Civil Engineering Festival 2026[^<]*<em>[^<]*<\/em>\.<\/p>',
}

for key, pattern in old_descriptions.items():
    new_desc = descriptions[key]
    new_content = re.sub(pattern, new_desc, content, flags=re.DOTALL)
    if new_content != content:
        print(f"  Updated {key.upper()} description")
        content = new_content
    else:
        print(f"  WARNING: {key.upper()} description not found - may already be updated")

# Also fix NBMDC logo scale in detail-nbmdc
content = content.replace(
    '<div class="comp-logo"><img src="/lombatra/NBMDC.png" alt="NBMDC Logo" />',
    '<div class="comp-logo"><img src="/lombatra/NBMDC.png" alt="NBMDC Logo" style="transform: scale(1.5);" />'
)

with open('register.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! register.html updated.")
