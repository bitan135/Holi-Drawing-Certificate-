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
# Reduced from 1056x746 q75 to 528x373 q50 to cut memory 4x for mobile html2canvas
# CSS background-size:cover upscales it — visual quality stays identical
bg_img = bg_img.resize((528, 373), Image.Resampling.LANCZOS)
bg_buffer = io.BytesIO()
if bg_img.mode in ('RGBA', 'P'):
    bg_img = bg_img.convert('RGB')
bg_img.save(bg_buffer, format="JPEG", quality=50)
bg_b64 = base64.b64encode(bg_buffer.getvalue()).decode("utf-8")
bg_data_uri = f"data:image/jpeg;base64,{bg_b64}"

# 2. Intricate Traditional Alpona SVG Borders (Base64 encoded for html2canvas)
svg_h = """<svg width="80" height="28" viewBox="0 0 80 28" xmlns="http://www.w3.org/2000/svg">
  <path d="M0,14 C10,2 20,2 30,14 C20,26 10,26 0,14 Z" fill="none" stroke="#b8860b" stroke-width="1.2" opacity="0.9"/>
  <path d="M5,14 C12,6 18,6 25,14 C18,22 12,22 5,14 Z" fill="#e8b030" opacity="0.3"/>
  <ellipse cx="15" cy="14" rx="4" ry="6" fill="none" stroke="#7a0030" stroke-width="0.8" opacity="0.7"/>
  <circle cx="15" cy="14" r="2" fill="#7a0030" opacity="0.5"/>
  <path d="M40,14 C50,2 60,2 70,14 C60,26 50,26 40,14 Z" fill="none" stroke="#b8860b" stroke-width="1.2" opacity="0.9"/>
  <path d="M45,14 C52,6 58,6 65,14 C58,22 52,22 45,14 Z" fill="#e8b030" opacity="0.3"/>
  <ellipse cx="55" cy="14" rx="4" ry="6" fill="none" stroke="#7a0030" stroke-width="0.8" opacity="0.7"/>
  <circle cx="55" cy="14" r="2" fill="#7a0030" opacity="0.5"/>
  <circle cx="35" cy="14" r="2.5" fill="#c8960c" opacity="0.8"/>
  <circle cx="35" cy="6" r="1" fill="#7a0030" opacity="0.5"/>
  <circle cx="35" cy="22" r="1" fill="#7a0030" opacity="0.5"/>
  <line x1="0" y1="1" x2="80" y2="1" stroke="#c8960c" stroke-width="0.5" opacity="0.6"/>
  <line x1="0" y1="27" x2="80" y2="27" stroke="#c8960c" stroke-width="0.5" opacity="0.6"/>
</svg>"""
alpona_h_uri = f"data:image/svg+xml;base64,{base64.b64encode(svg_h.encode('utf-8')).decode('utf-8')}"

svg_v = """<svg width="28" height="80" viewBox="0 0 28 80" xmlns="http://www.w3.org/2000/svg">
  <path d="M14,0 C2,10 2,20 14,30 C26,20 26,10 14,0 Z" fill="none" stroke="#b8860b" stroke-width="1.2" opacity="0.9"/>
  <path d="M14,5 C6,12 6,18 14,25 C22,18 22,12 14,5 Z" fill="#e8b030" opacity="0.3"/>
  <ellipse cx="14" cy="15" rx="6" ry="4" fill="none" stroke="#7a0030" stroke-width="0.8" opacity="0.7"/>
  <circle cx="14" cy="15" r="2" fill="#7a0030" opacity="0.5"/>
  <path d="M14,40 C2,50 2,60 14,70 C26,60 26,50 14,40 Z" fill="none" stroke="#b8860b" stroke-width="1.2" opacity="0.9"/>
  <path d="M14,45 C6,52 6,58 14,65 C22,58 22,52 14,45 Z" fill="#e8b030" opacity="0.3"/>
  <ellipse cx="14" cy="55" rx="6" ry="4" fill="none" stroke="#7a0030" stroke-width="0.8" opacity="0.7"/>
  <circle cx="14" cy="55" r="2" fill="#7a0030" opacity="0.5"/>
  <circle cx="14" cy="35" r="2.5" fill="#c8960c" opacity="0.8"/>
  <circle cx="6" cy="35" r="1" fill="#7a0030" opacity="0.5"/>
  <circle cx="22" cy="35" r="1" fill="#7a0030" opacity="0.5"/>
  <line x1="1" y1="0" x2="1" y2="80" stroke="#c8960c" stroke-width="0.5" opacity="0.6"/>
  <line x1="27" y1="0" x2="27" y2="80" stroke="#c8960c" stroke-width="0.5" opacity="0.6"/>
</svg>"""
alpona_v_uri = f"data:image/svg+xml;base64,{base64.b64encode(svg_v.encode('utf-8')).decode('utf-8')}"

html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>আবার বসন্ত ২০২৬ - শংসাপত্র</title>
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
    background-color: #1a1a1a;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Noto Sans Bengali', sans-serif;
  }}



  /* Scaling wrapper */
  .scale-wrapper {{
    width: 1587px;
    height: 1123px;
    transform-origin: top center;
  }}

  /* ═══ CERTIFICATE ═══ */
  #certificate {{
    width: 1587px;
    height: 1123px;
    position: relative;
    background-color: #fffaf0;
    overflow: hidden;
    box-sizing: border-box;
  }}

  /* ── MULTI-LAYER BORDER SYSTEM ── */
  .border-outer {{
    position: absolute;
    inset: 0;
    border: 10px solid #b8860b;
    z-index: 5;
    pointer-events: none;
  }}
  .border-cream {{
    position: absolute;
    inset: 10px;
    border: 4px solid #fffdf5;
    z-index: 6;
    pointer-events: none;
  }}
  .border-inner-gold {{
    position: absolute;
    inset: 14px;
    border: 2px solid #c8960c;
    z-index: 7;
    pointer-events: none;
  }}
  .alpona-strip {{
    position: absolute;
    inset: 20px;
    z-index: 8;
    pointer-events: none;
  }}
  .alpona-edge {{
    position: absolute;
    background-repeat: repeat;
  }}
  .alpona-top, .alpona-bottom {{
    left: 0; right: 0;
    height: 28px;
    background-image: url("{alpona_h_uri}");
    background-size: 80px 28px;
    background-repeat: repeat-x;
  }}
  .alpona-left, .alpona-right {{
    top: 0; bottom: 0;
    width: 28px;
    background-image: url("{alpona_v_uri}");
    background-size: 28px 80px;
    background-repeat: repeat-y;
  }}
  .alpona-top  {{ top: 0; }}
  .alpona-bottom {{ bottom: 0; }}
  .alpona-left {{ left: 0; }}
  .alpona-right {{ right: 0; }}
  .border-inner-crimson {{
    position: absolute;
    inset: 48px;
    border: 1px solid rgba(122,0,48,0.35);
    z-index: 9;
    pointer-events: none;
  }}

  /* Corner Ornaments */
  .corner-ornament {{
    position: absolute;
    font-family: serif;
    font-size: 38px;
    color: #c8960c;
    z-index: 15;
    line-height: 1;
    text-shadow: 0 2px 5px rgba(122,0,48,0.5);
  }}
  .corner-tl {{ top: 50px; left: 52px; }}
  .corner-tr {{ top: 50px; right: 52px; }}
  .corner-bl {{ bottom: 50px; left: 52px; }}
  .corner-br {{ bottom: 50px; right: 52px; }}

  /* ── BACKGROUND LAYERS ── */
  .bg-image {{
    position: absolute;
    inset: 0;
    background-image: url("{bg_data_uri}");
    background-size: cover;
    background-position: center;
    filter: saturate(1.6) contrast(1.1) brightness(1.05);
    z-index: 1;
  }}
  .bg-vignette {{
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 75% 65% at 50% 50%, rgba(255,250,240,0.72) 0%, rgba(255,250,240,0.65) 45%, rgba(255,250,240,0.3) 80%, transparent 100%);
    z-index: 2;
  }}

  /* ── CONTENT LAYOUT ── */
  .cert-content {{
    position: relative;
    z-index: 20;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    padding: 85px 130px 65px 130px;
    box-sizing: border-box;
  }}

  /* Section 1: Header */
  .header-block {{
    text-align: center;
    margin-top: 5px;
  }}
  .main-title {{
    font-family: 'Noto Serif Bengali', serif;
    font-weight: 900;
    font-size: 62pt;
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
    font-size: 17pt;
    color: #3a1500;
    margin: 12px 0 0 0;
    letter-spacing: normal;
    text-shadow: 0 1px 6px rgba(255,250,240,1);
  }}

  /* Section 2: Gold Divider */
  .gold-divider {{
    width: 60%;
    height: 2px;
    margin: 0 auto;
    background: linear-gradient(to right, transparent, #f5d060, #c8960c, #f5d060, transparent);
    box-shadow: 0 0 10px rgba(200,150,12,0.5);
  }}

  /* Section 3: Body Text */
  .body-text-box {{
    padding: 10px 30px 25px 30px;
    text-align: center;
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 600;
    font-size: 22pt;
    color: #120808;
    line-height: 2.2;
    margin: 0 auto;
    width: 95%;
    letter-spacing: normal;
    text-rendering: optimizeLegibility;
    text-shadow: 0 2px 10px rgba(255,250,240,0.95), 0 0 15px rgba(255,250,240,0.8);
  }}
  .body-text-line-wrapper {{
    margin-top: 25px;
  }}
  .blank {{
    display: inline-block;
    border-bottom: 3px solid #3a1500;
    vertical-align: text-bottom;
    text-align: center;
    padding: 0 10px;
    color: #7a0030;
    font-weight: 800;
  }}

  /* Section 4: Date & Place */
  .date-place {{
    display: flex;
    justify-content: space-between;
    width: 75%;
    margin: 0 auto;
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 700;
    font-size: 18pt;
    color: #3a1500;
    text-shadow: 0 1px 5px rgba(255,250,240,1);
  }}

  /* Section 5: Signatures */
  .signature-block {{
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 25px;
    padding: 0 30px;
  }}
  .sig-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .sig-line-wrapper {{
    position: relative;
    width: 130px;
    margin-bottom: 18px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .sig-line-wrapper::before {{
    content: '\u2726';
    color: #c8960c;
    font-size: 14pt;
    position: absolute;
    top: -26px;
    text-shadow: 0 1px 2px rgba(120,0,40,0.4);
  }}
  .sig-line {{
    width: 100%;
    border-top: 3px solid #7a0030;
  }}
  .sig-role {{
    font-family: 'Noto Sans Bengali', sans-serif;
    font-weight: 900;
    font-size: 26pt;
    color: #7a0030;
    letter-spacing: normal;
    text-shadow: 0 3px 8px rgba(120,0,40,0.5);
    background: rgba(255, 250, 240, 0.88);
    padding: 4px 30px;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-top: 4px;
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

  /* Print */
  @media print {{
    body {{ background: none; padding: 0; }}
    .downloadBtn, .controls-wrapper {{ display: none; }}
    .scale-wrapper {{ transform: none !important; width: 297mm; height: 210mm; }}
    #certificate {{ width: 297mm; height: 210mm; }}
  }}
</style>
</head>
<body>



  <div class="scale-wrapper" id="scaleWrapper">
    <div id="certificate">
      <!-- Backgrounds -->
      <div class="bg-image"></div>
      <div class="bg-vignette"></div>

      <!-- Multi-Layer Border System -->
      <div class="border-outer"></div>
      <div class="border-cream"></div>
      <div class="border-inner-gold"></div>
      <div class="alpona-strip">
        <div class="alpona-edge alpona-top"></div>
        <div class="alpona-edge alpona-bottom"></div>
        <div class="alpona-edge alpona-left"></div>
        <div class="alpona-edge alpona-right"></div>
      </div>
      <div class="border-inner-crimson"></div>

      <!-- Corner Ornaments -->
      <div class="corner-ornament corner-tl">\u2767</div>
      <div class="corner-ornament corner-tr">\u2767</div>
      <div class="corner-ornament corner-bl">\u2767</div>
      <div class="corner-ornament corner-br">\u2767</div>

      <!-- Content -->
      <div class="cert-content">

        <!-- 1. Header -->
        <div class="header-block">
          <div class="main-title">\u0986\u09ac\u09be\u09b0 \u09ac\u09b8\u09a8\u09cd\u09a4, \u09e8\u09e6\u09e8\u09ec</div>
          <div class="organizer">\u09aa\u09b0\u09bf\u099a\u09be\u09b2\u09a8\u09be\u09af\u09bc: \u09e7\u09ec \u09a8\u09ae\u09cd\u09ac\u09b0 \u0993\u09af\u09bc\u09be\u09b0\u09cd\u09a1 \u09ac\u09b8\u09a8\u09cd\u09a4 \u0989\u09ce\u09b8\u09ac \u0995\u09ae\u09bf\u099f\u09bf</div>
        </div>

        <!-- 2. Divider -->
        <div class="gold-divider"></div>

        <!-- 3. Body Text -->
        <div class="body-text-box">
          <div class="body-text-line-wrapper">
            <span class="blank" style="min-width: 260px;"></span> \u09aa\u09cd\u09b0\u09a4\u09bf\u09af\u09cb\u0997\u09bf\u09a4\u09be\u09af\u09bc <span class="blank" style="min-width: 200px;"></span> \u09ac\u09bf\u09ad\u09be\u0997\u09c7 <span class="blank" style="min-width: 140px;"></span> \u09b8\u09cd\u09a5\u09be\u09a8\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c0
          </div>
          <div class="body-text-line-wrapper">
            \u09b6\u09cd\u09b0\u09c0/\u09b6\u09cd\u09b0\u09c0\u09ae\u09a4\u09c0 <span class="blank" style="min-width: 580px;"></span> \u0995\u09c7 \u09b6\u0982\u09b8\u09be\u09aa\u09a4\u09cd\u09b0 \u09aa\u09cd\u09b0\u09a6\u09a4\u09cd\u09a4 \u09b9\u09b2\u0964
          </div>
        </div>

        <!-- 4. Date & Place -->
        <div class="date-place">
          <div>\u09a4\u09be\u09b0\u09bf\u0996: <span class="blank" style="min-width: 140px;"></span></div>
          <div>\u09b8\u09cd\u09a5\u09be\u09a8: <span style="margin-left:8px;">\u09ae\u09cb\u0982\u09b2\u09be\u09aa\u09be\u09a1\u09bc\u09be \u09ae\u09be\u09a0</span></div>
        </div>

        <!-- 5. Signatures -->
        <div class="signature-block">
          <div class="sig-col">
            <div class="sig-line-wrapper"><div class="sig-line"></div></div>
            <div class="sig-role">\u09b8\u09ad\u09be\u09aa\u09a4\u09bf</div>
          </div>
          <div class="sig-col">
            <div class="sig-line-wrapper"><div class="sig-line"></div></div>
            <div class="sig-role">\u09b8\u09ae\u09cd\u09aa\u09be\u09a6\u0995</div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <button class="downloadBtn" id="downloadBtn">Download Certificate (PNG)</button>

  <script>


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
    resizeCertificate();

    document.getElementById('downloadBtn').addEventListener('click', async () => {{
      const btn = document.getElementById('downloadBtn');
      const originalText = btn.innerText;
      const resetBtn = () => {{ btn.innerText = originalText; btn.style.opacity = '1'; btn.style.pointerEvents = 'auto'; }};

      btn.innerText = 'Generating...';
      btn.style.opacity = '0.7';
      btn.style.pointerEvents = 'none';

      try {{
        await document.fonts.ready;

        const isMobile = /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent) || window.innerWidth <= 768;
        const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);

        // Mobile: 1x scale + JPEG = minimal memory (~2MB total)
        // Desktop: 4x scale + PNG = ultra print quality
        const exportScale = isMobile ? 1 : 4;
        const exportFormat = isMobile ? 'image/jpeg' : 'image/png';
        const exportQuality = isMobile ? 0.92 : 1.0;
        const exportExt = isMobile ? 'jpg' : 'png';

        const cert = document.getElementById('certificate');
        const canvas = await html2canvas(cert, {{
          scale: exportScale,
          useCORS: true,
          allowTaint: true,
          backgroundColor: '#fffaf0',
          logging: false,
          imageTimeout: 0,
          onclone: function(clonedDoc) {{
            var sw = clonedDoc.getElementById('scaleWrapper');
            if (sw) {{ sw.style.transform = 'none'; sw.style.marginBottom = '0'; }}
          }}
        }});

        // Convert canvas to blob using Promise for proper error handling
        const blob = await new Promise(function(resolve, reject) {{
          try {{
            canvas.toBlob(function(b) {{
              if (b) resolve(b);
              else reject(new Error('Blob conversion failed'));
            }}, exportFormat, exportQuality);
          }} catch(e) {{
            reject(e);
          }}
        }});

        const blobUrl = URL.createObjectURL(blob);

        if (isIOS) {{
          // iOS Safari: navigate to blob URL, user long-presses to save
          window.location.href = blobUrl;
        }} else {{
          // Android + Desktop: standard download
          var a = document.createElement('a');
          a.href = blobUrl;
          a.download = 'certificate.' + exportExt;
          a.style.display = 'none';
          document.body.appendChild(a);
          a.click();
          setTimeout(function() {{ document.body.removeChild(a); URL.revokeObjectURL(blobUrl); }}, 2000);
        }}

        resetBtn();

      }} catch (err) {{
        console.error('Download error:', err);
        alert('Download failed: ' + err.message + '. Try using a desktop browser.');
        resetBtn();
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
