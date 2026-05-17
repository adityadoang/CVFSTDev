import re

with open('register.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Map of comp ID to correct registration link
comp_links = {
    'detail-nbmdc': 'https://bit.ly/Pendaftaran_NBMDC_Civfest2026',
    'detail-nptc':  'https://bit.ly/NPTC_CIVFEST2026',
    'detail-nbdc':  'https://bit.ly/NBDC_CIVFEST2026',
    'detail-ncc':   'https://bit.ly/PendaftaranNCCcivfest2026',
    'detail-nbc':   'https://bit.ly/FormulirPendaftaranNBC2026',
}

# Also update TOR guide links (all -> LombaCivfest2026, except NBMDC which uses drive)
tor_link = 'https://bit.ly/LombaCivfest2026'

# Split content by comp-detail-content div
pattern = r'(<div class="comp-detail-content" id=")(detail-[a-z]+)(")'

def replace_in_block(m, block_id, block_content):
    """Replace link in block content."""
    reg_link = comp_links.get(block_id, '#')
    # Replace old register link
    block_content = re.sub(
        r'href="https://bit\.ly/NBMDC_CIVFEST2025"',
        f'href="{reg_link}"',
        block_content
    )
    # Update price: Rp. 150.000 -> 200.000 with data attribute (for non-NBMDC)
    if block_id != 'detail-nbmdc':
        block_content = block_content.replace(
            '<span class="stat-value">Rp. 150.000,00 / team</span>',
            '<span class="stat-value price-display" data-base-price="200000">Rp. 200.000,00 / team</span>'
        )
    else:
        block_content = block_content.replace(
            '<span class="stat-value">Rp. 150.000,00 / team</span>',
            '<span class="stat-value price-display" data-base-price="150000">Rp. 150.000,00 / team</span>'
        )
    # Replace TOR Guide href="#" with proper link
    block_content = block_content.replace(
        'href="#" class="btn-secondary">TOR Guide</a>',
        f'href="{tor_link}" target="_blank" class="btn-secondary">TOR Guide</a>'
    )
    # Fix drive link for NBMDC
    if block_id == 'detail-nbmdc':
        block_content = block_content.replace(
            f'href="{tor_link}" target="_blank" class="btn-secondary">TOR Guide</a>',
            f'href="{tor_link}" target="_blank" class="btn-secondary">TOR Guide</a>'
        )
    return block_content

# Process each comp block
result = content
for comp_id, reg_link in comp_links.items():
    # Find the block start
    start_tag = f'<div class="comp-detail-content" id="{comp_id}"'
    start_pos = result.find(start_tag)
    if start_pos == -1:
        print(f"NOT FOUND: {comp_id}")
        continue
    
    # Find the closing </div> for this block (search for the next comp block or end of detail-view)
    block_start = start_pos
    # Find next comp-detail-content or </div> that closes this
    # Use a simple approach: find the next occurrence of comp-detail-content or comp-back-btn
    search_from = start_pos + len(start_tag)
    next_block = result.find('<div class="comp-detail-content"', search_from)
    end_marker = result.find('</div>\n\n            </div>', search_from)  # End of last block
    
    if next_block != -1:
        block_end = next_block
    elif end_marker != -1:
        block_end = end_marker + 6  # Include the </div>
    else:
        print(f"Could not find end for: {comp_id}")
        continue
    
    block = result[block_start:block_end]
    
    # Replace register link
    new_block = re.sub(
        r'href="https://bit\.ly/NBMDC_CIVFEST2025"',
        f'href="{reg_link}"',
        block
    )
    
    # Replace registration fee and price
    if comp_id != 'detail-nbmdc':
        new_block = new_block.replace(
            '<span class="stat-value">Rp. 150.000,00 / team</span>',
            '<span class="stat-value price-display" data-base-price="200000">Rp. 200.000,00 / team</span>'
        )
    else:
        new_block = new_block.replace(
            '<span class="stat-value">Rp. 150.000,00 / team</span>',
            '<span class="stat-value price-display" data-base-price="150000">Rp. 150.000,00 / team</span>'
        )
    
    # Fix TOR link
    new_block = new_block.replace(
        'href="#" class="btn-secondary">TOR Guide</a>',
        f'href="{tor_link}" target="_blank" class="btn-secondary">TOR Guide</a>'
    )
    
    result = result[:block_start] + new_block + result[block_end:]
    print(f"Fixed: {comp_id}")

# Count remaining old links
remaining = result.count('NBMDC_CIVFEST2025')
print(f"\nRemaining old links: {remaining}")

with open('register.html', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done!")
