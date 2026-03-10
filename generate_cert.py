import base64
from PIL import Image
import io
import os

# 1. Base Background Image
bg_path = "/Users/bitanbiswas/.gemini/antigravity/brain/7801b942-32ca-46e3-aee4-792673f45c28/holi_cert_borderless_premium_1773156264221.png"
if not os.path.exists(bg_path):
    print("Background image not found:", bg_path)
    exit(1)

bg_img = Image.open(bg_path)
bg_img = bg_img.resize((1056, 746), Image.Resampling.LANCZOS)
bg_buffer = io.BytesIO()
if bg_img.mode in ('RGBA', 'P'):
    bg_img = bg_img.convert('RGB')
bg_img.save(bg_buffer, format="JPEG", quality=75)
bg_b64 = base64.b64encode(bg_buffer.getvalue()).decode("utf-8")
bg_data_uri = f"data:image/jpeg;base64,{bg_b64}"

# 2. Logo Image for base64 injection
logo_path = "/Users/bitanbiswas/.gemini/antigravity/brain/7801b942-32ca-46e3-aee4-792673f45c28/media__1773160432503.png"
logo_data_uri = ""
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    # Resize logo appropriately (72x72 is approx 200x200 at full export res)
    logo_img = logo_img.resize((200, 200), Image.Resampling.LANCZOS)
    logo_buffer = io.BytesIO()
    # Save as PNG to maintain transparency
    logo_img.save(logo_buffer, format="PNG")
    logo_b64 = base64.b64encode(logo_buffer.getvalue()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"


html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>আবার বসন্ত ২০২৬ - প্রশস্তিকা</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Bengali:wght@400;600;700;900&family=Noto+Sans+Bengali:wght@400;500;600;700;900&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>
  @page {{
    size: 297mm 210mm landscape;
    margin: 0;
  }}
  body {{
    margin: 0;
    padding: 20px 0 40px 0;
    background-color: #2c2c2c;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Noto Sans Bengali', sans-serif;
  }}
  
  /* Top Controls Area for the Toggle */
  .controls-wrapper {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-bottom: 25px;
    background: #1a1a1a;
    padding: 12px 24px;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    z-index: 100;
  }}
  .toggle-type-btn {{
    background: transparent;
    border: 2px solid #c8960c;
    color: #c8960c;
    font-family: 'Noto Sans Bengali', sans-serif;
    font-size: 13pt;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.2s ease;
  }}
  .toggle-type-btn.active {{
    background: linear-gradient(135deg, #c8960c, #f5d060, #c8960c);
    color: #3a1500;
    box-shadow: 0 4px 12px rgba(200,150,12,0.4);
    border-color: transparent;
  }}

  /* Scaling wrapper for mobile/desktop display */
  .scale-wrapper {{
    width: 1587px;
    height: 1123px;
    transform-origin: top center;
  }}
  #certificate {{
    width: 1587px;
    height: 1123px;
    position: relative;
    background-color: #fffaf0;
    overflow: hidden;
    /* Outermost premium border */
    box-shadow: inset 0 0 0 8px #d4a017, inset 0 0 0 12px #fffaf0, inset 0 0 0 14px #c8960c, inset 0 0 25px 14px rgba(0,0,0,0.15), 0 15px 50px rgba(0,0,0,0.5);
    box-sizing: border-box;
  }}
  
  /* Background Layers */
  .bg-image {{
    position: absolute;
    inset: 0;
    background-image: url("{bg_data_uri}");
    background-size: cover;
    background-position: center;
    /* CHANGE 7: Vibrancy Filters */
    filter: saturate(1.6) contrast(1.1) brightness(1.05);
    z-index: 1;
  }}
  .bg-vignette {{
    position: absolute;
    inset: 0;
    /* CHANGE 7: more transparent center */
    background: radial-gradient(ellipse 75% 65% at 50% 50%, rgba(255,250,240,0.72) 0%, rgba(255,250,240,0.65) 45%, rgba(255,250,240,0.3) 80%, transparent 100%);
    z-index: 2;
  }}

  /* CHANGE 8: Logo Placement Refined */
  .cert-logo {{
    position: absolute;
    top: 68px; /* ~18mm scaled */
    left: 75px; /* ~20mm scaled */
    width: 85px; /* Slightly larger */
    height: 85px;
    object-fit: contain;
    background: rgba(255, 250, 240, 0.85); /* Premium frosted cream */
    border: 2px solid #c8960c; /* Matching gold ring */
    border-radius: 50%;
    padding: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15), inset 0 0 8px rgba(255,255,255,0.8);
    z-index: 25; /* above everything */
  }}

  /* CHANGE 2: Refined Traditional Alpona-style Decorative Border */
  /* Replaced raw unicode characters with an elegant, hand-crafted CSS geometric pattern that mimics traditional Indian/Bengali motifs */
  .alpona-strip {{
    position: absolute;
    inset: 22px; /* Just barely inside the 14px gold box-shadow border */
    border: 6px solid transparent;
    /* An elegant repeating diamond/dot motif using CSS gradients */
    border-image: repeating-radial-gradient(
      circle at 0 0,
      transparent 0,
      transparent 5px,
      #c8960c 6px,
      #c8960c 7px,
      transparent 8px
    ) 12;
    padding: 4px;
    z-index: 10;
    pointer-events: none;
  }}
  .alpona-inner {{
     /* A secondary inner border to frame the Alpona pattern */
     position: absolute;
     inset: 4px;
     border: 1px dotted #7a0030;
     opacity: 0.6;
  }}
  
  /* Corner Ornaments */
  .corner-ornament {{
    position: absolute;
    font-family: serif;
    font-size: 36px;
    color: #c8960c;
    z-index: 15;
    line-height: 1;
    text-shadow: 0 2px 4px rgba(122,0,48,0.4);
  }}
  .corner-tl {{ top: 38px; left: 42px; }}
  .corner-tr {{ top: 38px; right: 42px; }}
  .corner-bl {{ bottom: 38px; left: 42px; }}
  .corner-br {{ bottom: 38px; right: 42px; }}

  /* Content Layout */
  .cert-content {{
    position: relative;
    z-index: 20;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    /* Keep padding inside the Alpona strip */
    padding: 80px 125px 68px 125px;
    box-sizing: border-box;
  }}

  /* Section 1: Header */
  .header-block {{
    text-align: center;
    margin-top: 10px;
  }}
  .main-title {{
    font-family: 'Noto Serif Bengali', serif;
    font-weight: 900;
    font-size: 64pt;
    color: #7a0030;
    margin: 0;
    line-height: 1.2;
    letter-spacing: normal;
    text-rendering: optimizeLegibility;
    text-shadow: 0 4px 15px rgba(255,250,240,0.95), 0 2px 5px rgba(0,0,0,0.2);
  }}
  .organizer {{
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 600;
    font-size: 16pt;
    color: #3a1500;
    margin: 10px 0 0 0;
    letter-spacing: normal;
    text-shadow: 0 1px 5px rgba(255,250,240,1);
  }}

  /* Section 2: Gold Divider */
  .gold-divider {{
    width: 65%;
    height: 2px;
    margin: 0 auto;
    background: linear-gradient(to right, transparent, #f5d060, #c8960c, #f5d060, transparent);
    box-shadow: 0 0 10px rgba(200,150,12,0.5);
  }}

  /* Section 3: Body Text box */
  .body-text-box {{
    padding: 18px 30px;
    text-align: center;
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 600; 
    font-size: 20pt; 
    color: #120808;
    line-height: 2.4;
    margin: 0 auto;
    width: 95%;
    letter-spacing: normal;
    text-rendering: optimizeLegibility;
    text-shadow: 0 2px 10px rgba(255,250,240,0.95);
  }}
  .blank {{
    display: inline-block;
    border-bottom: 2px solid #3a1500;
    transform: translateY(2px);
    text-align: center;
    padding: 0 10px;
    color: #7a0030;
    font-weight: 700;
  }}

  /* Section 4: Date & Place */
  .date-place {{
    display: flex;
    justify-content: space-between;
    width: 75%; 
    margin: 0 auto; 
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 700;
    font-size: 16pt;
    color: #3a1500;
    text-shadow: 0 1px 5px rgba(255,250,240,1);
  }}

  /* Section 5: Signatures */
  .signature-block {{
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 30px;
  }}
  .sig-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  /* CHANGE 3: Add ornament above signature lines */
  .sig-line-wrapper {{
    position: relative;
    width: 80px; 
    margin-bottom: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .sig-line-wrapper::before {{
    content: '✦'; /* small gold ornament */
    color: #c8960c;
    font-size: 12pt;
    position: absolute;
    top: -24px;
    text-shadow: 0 1px 2px rgba(120,0,40,0.2);
  }}
  .sig-line {{
    width: 100%;
    border-top: 3px solid #7a0030; /* Thicker bold line */
  }}
  .sig-role {{
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 900;
    font-size: 20pt; /* Much larger and more prominent */
    color: #7a0030;
    letter-spacing: normal;
    text-shadow: 0 2px 6px rgba(120,0,40,0.4);
    margin-top: 6px;
  }}

  /* Download Button */
  .downloadBtn {{
    background: linear-gradient(135deg, #c8960c, #f5d060, #c8960c);
    color: #3a1500;
    font-family: 'Noto Sans Bengali', sans-serif;
    font-size: 14pt;
    font-weight: 700;
    padding: 14px 48px;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0 6px 24px rgba(200,150,12,0.4);
    margin-top: 28px;
    letter-spacing: 1px;
    transition: transform 0.2s, box-shadow 0.2s;
    z-index: 100;
  }}
  .downloadBtn:hover {{
    transform: scale(1.04);
    box-shadow: 0 8px 30px rgba(200,150,12,0.6);
  }}

  /* Print Media Query */
  @media print {{
    body {{ background: none; padding: 0; }}
    .downloadBtn, .controls-wrapper {{ display: none; }}
    .scale-wrapper {{ transform: none !important; width: 297mm; height: 210mm; }}
    #certificate {{ width: 297mm; height: 210mm; box-shadow: none; }}
  }}
</style>
</head>
<body>

  <!-- Customization Toggle UI -->
  <div class="controls-wrapper">
    <button id="btn-ankon" class="toggle-type-btn active" onclick="setCertType('অঙ্কন')">অঙ্কন প্রতিযোগিতা</button>
    <button id="btn-fashion" class="toggle-type-btn" onclick="setCertType('ফ্যাশন')">ফ্যাশন প্রতিযোগিতা</button>
  </div>

  <div class="scale-wrapper" id="scaleWrapper">
    <div id="certificate">
      <!-- Backgrounds -->
      <div class="bg-image"></div>
      <div class="bg-vignette"></div>
      
      <!-- Logo -->
      <img src="{logo_data_uri}" class="cert-logo" alt="Logo" />

      <!-- Alpona Decorative Border -->
      <div class="alpona-strip">
        <div class="alpona-inner"></div>
      </div>
      
      <!-- Corner Ornaments ❧ -->
      <div class="corner-ornament corner-tl">❧</div>
      <div class="corner-ornament corner-tr">❧</div>
      <div class="corner-ornament corner-bl">❧</div>
      <div class="corner-ornament corner-br">❧</div>

      <!-- Content -->
      <div class="cert-content">
        
        <!-- 1. Header (No subtitle) -->
        <div class="header-block">
          <div class="main-title">আবার বসন্ত, ২০২৬</div>
          <div class="organizer">পরিচালনায়: ১৬ নম্বর ওয়ার্ড বসন্ত উৎসব কমিটি</div>
        </div>

        <!-- 2. Divider -->
        <div class="gold-divider"></div>

        <!-- 3. Body Text (CHANGE 4: Adjusted min-widths, CHANGE 6: Wording) -->
        <div class="body-text-box">
          <span class="blank" id="blankType" style="min-width: 220px;">অঙ্কন</span> প্রতিযোগিতায় <span class="blank" style="min-width: 160px;"></span> বিভাগে <span class="blank" style="min-width: 120px;"></span> স্থানাধিকারী<br>
          শ্রী/শ্রীমতী <span class="blank" style="min-width: 420px;"></span> কে শংসাপত্র প্রদত্ত হল।
        </div>

        <!-- 4. Date & Place (CHANGE 5: No underline for Location limit) -->
        <div class="date-place">
          <div>তারিখ: <span class="blank" style="min-width: 140px;"></span></div>
          <div>স্থান: <span style="margin-left:8px;">মোংলাপাড়া মাঠ</span></div>
        </div>

        <!-- 5. Signatures (CHANGE 3: Bold, Ornaments) -->
        <div class="signature-block">
          <div class="sig-col">
            <div class="sig-line-wrapper"><div class="sig-line"></div></div>
            <div class="sig-role">সভাপতি</div>
          </div>
          <div class="sig-col">
            <div class="sig-line-wrapper"><div class="sig-line"></div></div>
            <div class="sig-role">সম্পাদক</div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <button class="downloadBtn" id="downloadBtn">Download Certificate (PNG)</button>

  <script>
    // JS Logic for Toggle Type
    function setCertType(typeStr) {{
      document.getElementById('blankType').innerText = typeStr;
      if (typeStr === 'অঙ্কন') {{
        document.getElementById('btn-ankon').classList.add('active');
        document.getElementById('btn-fashion').classList.remove('active');
      }} else {{
        document.getElementById('btn-fashion').classList.add('active');
        document.getElementById('btn-ankon').classList.remove('active');
      }}
    }}

    // Scale the wrapper to fit nicely on the user's screen
    function resizeCertificate() {{
      const wrapper = document.getElementById('scaleWrapper');
      const windowWidth = window.innerWidth;
      const windowHeight = window.innerHeight;
      const scaleX = (windowWidth - 40) / 1587;
      const scaleY = (windowHeight - 160) / 1123;
      const scale = Math.min(scaleX, scaleY, 1);
      wrapper.style.transform = `scale(${{scale}})`;
      wrapper.style.marginBottom = `-${{1123 * (1 - scale)}}px`;
    }}
    
    window.addEventListener('resize', resizeCertificate);
    resizeCertificate(); // initial call

    // Download Logic via html2canvas
    document.getElementById('downloadBtn').addEventListener('click', async () => {{
      const btn = document.getElementById('downloadBtn');
      const originalText = btn.innerText;
      btn.innerText = "Generating PNG... (This may take a moment)";
      btn.style.opacity = "0.7";
      btn.style.pointerEvents = "none";

      try {{
        const cert = document.getElementById('certificate');
        await document.fonts.ready;
        await new Promise(resolve => setTimeout(resolve, 300));

        const isMobile = window.innerWidth <= 768;
        const exportScale = isMobile ? 2.5 : 4;

        const canvas = await html2canvas(cert, {{
          scale: exportScale,
          useCORS: true,
          backgroundColor: null,
          logging: false,
          letterRendering: 1, 
          onclone: function(clonedDoc) {{
            const scaleWrap = clonedDoc.getElementById('scaleWrapper');
            if (scaleWrap) {{
              scaleWrap.style.transform = 'none';
              scaleWrap.style.marginBottom = '0';
            }}
          }}
        }});
        
        canvas.toBlob((blob) => {{
          if (!blob) throw new Error("Canvas to Blob failed.");
          const blobUrl = URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.download = document.getElementById('btn-ankon').classList.contains('active') ? 'ankon_certificate.png' : 'fashion_certificate.png';
          link.href = blobUrl;
          document.body.appendChild(link);
          link.click();
          setTimeout(() => {{ document.body.removeChild(link); URL.revokeObjectURL(blobUrl); }}, 100);
          
          btn.innerText = originalText;
          btn.style.opacity = "1";
          btn.style.pointerEvents = "auto";
        }}, 'image/png', 1.0);

      }} catch (err) {{
        console.error(err);
        alert("Error generating PNG. Check console.");
        btn.innerText = originalText;
        btn.style.opacity = "1";
        btn.style.pointerEvents = "auto";
      }}
    }});
  </script>
</body>
</html>
"""

output_path = "/Users/bitanbiswas/Documents/Antigravety Projects/Holi Drawing Certificate/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File successfully created: {output_path}")

