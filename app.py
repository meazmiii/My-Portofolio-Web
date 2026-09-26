import streamlit as st

st.set_page_config(
  page_title="Portofolio Azmi Aziz",
  layout="wide",
  initial_sidebar_state="collapsed",
)
st.markdown("""
<style>
  .block-container {
    padding: 0rem !important;
    max-width: 100% !important;
  }
  header,
  footer,
  #MainMenu {
    visibility: hidden;
    height: 0;
  }
  .stApp {
    overflow: hidden;
  }
</style>
""", unsafe_allow_html=True)

html_final = """
<!doctype html>
<html lang="id" class="scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Azmi Aziz | Strategic Alchemist</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap");

      body {
        font-family: "Space Grotesk", sans-serif;
        background-color: #000;
        background-image: url("https://www.transparenttextures.com/patterns/micro-carbon.png");
      }

      .bento-card {
        background: rgba(10, 10, 10, 0.95);
        border: 1px solid rgba(130, 230, 55, 0.1);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        overflow: hidden;
      }

      .bento-card:hover {
        border-color: #82e637;
        box-shadow: 0 0 30px rgba(130, 230, 55, 0.1);
        transform: translateY(-8px); /* Sedikit lebih tinggi biar kerasa */
      }

      /* FIX: Horizontal Scroll Mobile dengan Ruang Animasi */
      .project-scroll {
        display: flex;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        gap: 1.25rem;
        /* Tambahin padding top biar pas kartu naik/hover nggak kepotong */
        padding: 20px 10px;
        margin-left: -10px;
        margin-right: -10px;
      }

      /* Sembunyiin scrollbar tapi tetep bisa scroll */
      .project-scroll::-webkit-scrollbar {
        display: none;
      }
      .project-scroll {
        -ms-overflow-style: none;
        scrollbar-width: none;
      }

      .project-item {
        flex: 0 0 85%;
        scroll-snap-align: center;
      }

      @media (min-width: 768px) {
        .project-scroll {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          overflow-x: visible;
          padding: 0;
          margin: 0;
          gap: 1rem;
        }
        .project-item {
          flex: none;
        }
      }

      /* Hamburger Menu Logic */
      #menu-toggle:checked ~ #menu-items {
        display: flex;
        animation: slideIn 0.3s ease-out;
      }
      @keyframes slideIn {
        from {
          opacity: 0;
          transform: translateY(-10px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      .marquee-container {
        overflow: hidden;
        display: flex;
        align-items: center;
      }
      .marquee-content {
        display: flex;
        gap: 4rem;
        white-space: nowrap;
        animation: marquee 25s linear infinite;
      }
      @keyframes marquee {
        0% {
          transform: translateX(0);
        }
        100% {
          transform: translateX(-50%);
        }
      }
      .text-glow {
        text-shadow: 0 0 10px rgba(130, 230, 55, 0.3);
      }
      .animate-spin-slow {
        animation: spin 15s linear infinite;
      }
      @keyframes spin {
        from {
          transform: rotate(0deg);
        }
        to {
          transform: rotate(360deg);
        }
      }
      .dot-blink {
        animation: blink 1.5s infinite;
      }
      @keyframes blink {
        0%,
        100% {
          opacity: 1;
        }
        50% {
          opacity: 0.3;
        }
      }
    </style>
  </head>
  <body
    class="text-white selection:bg-[#82e637] selection:text-black p-4 md:p-10"
  >
    <main class="max-w-[1400px] mx-auto">
      <header
        class="relative flex justify-between items-center mb-10 border-b border-white/5 pb-6"
      >
        <div class="flex items-center gap-4">
          <div
            class="text-2xl font-extrabold tracking-tighter italic uppercase"
          >
            AZMI<span class="text-[#82e637]">.</span>AZIZ
          </div>
          <div
            class="flex items-center gap-1.5 bg-white/5 border border-white/10 px-2 py-1 rounded-md"
          >
            <span
              class="w-1 h-1 bg-[#82e637] rounded-full animate-pulse"
            ></span>
            <span
              class="text-[8px] font-bold text-gray-500 uppercase tracking-widest"
            >
              Hits: <span id="visitor-count" class="text-white">...</span>
            </span>
          </div>
        </div>

        <div class="md:hidden flex items-center">
          <input type="checkbox" id="menu-toggle" class="hidden" />
          <label
            for="menu-toggle"
            class="cursor-pointer p-2 flex flex-col gap-1.5 group"
          >
            <div class="w-6 h-0.5 bg-[#82e637]"></div>
            <div class="w-6 h-0.5 bg-[#82e637]"></div>
            <div class="w-6 h-0.5 bg-[#82e637]"></div>
          </label>

          <nav
            id="menu-items"
            class="hidden absolute top-full right-0 mt-2 flex-col bg-[#0a0a0a] border border-[#82e637]/20 rounded-2xl p-6 gap-4 z-50 text-[10px] uppercase tracking-widest min-w-[150px] shadow-2xl shadow-[#82e637]/10"
          >
            <a href="#experience" class="hover:text-[#82e637]">Experience</a>
            <a
              href="https://github.com/meazmiii"
              target="_blank"
              class="hover:text-[#82e637]"
              >GitHub</a
            >
            <a
              href="https://www.linkedin.com/in/azmi-aziz-719493240"
              target="_blank"
              class="hover:text-[#82e637]"
              >LinkedIn</a
            >
            <a
              href="https://www.instagram.com/_azmiazzz"
              target="_blank"
              class="hover:text-[#82e637]"
              >Instagram</a
            >
            <a
              href="https://wa.me/6283876788630"
              target="_blank"
              class="text-[#82e637]"
              >WhatsApp</a
            >
          </nav>
        </div>

        <nav
          class="hidden md:flex gap-6 text-[10px] uppercase tracking-[0.3em] font-bold text-gray-500"
        >
          <a
            href="#experience"
            class="hover:text-[#82e637] transition text-glow"
            >Experience</a
          >
          <a
            href="https://github.com/meazmiii"
            target="_blank"
            class="hover:text-[#82e637] transition text-glow"
            >GitHub</a
          >
          <a
            href="https://www.linkedin.com/in/azmi-aziz-719493240"
            target="_blank"
            class="hover:text-[#82e637] transition text-glow"
            >LinkedIn</a
          >
          <a
            href="https://www.instagram.com/_azmiazzz"
            target="_blank"
            class="hover:text-[#82e637] transition text-glow"
            >Instagram</a
          >
          <a
            href="https://wa.me/6283876788630"
            target="_blank"
            class="text-white border-b border-[#82e637]"
            >WhatsApp</a
          >
        </nav>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div
          class="md:col-span-3 bento-card p-10 md:p-16 rounded-[40px] flex flex-col justify-end min-h-[450px] relative"
        >
          <div class="absolute top-10 right-10 opacity-10">
            <svg
              width="150"
              height="150"
              viewBox="0 0 100 100"
              fill="none"
              class="animate-spin-slow"
            >
              <path
                d="M50 5 L55 45 L95 50 L55 55 L50 95 L45 55 L5 50 L45 45 Z"
                stroke="#82e637"
                stroke-width="0.5"
              />
            </svg>
          </div>
          <h1
            class="text-6xl md:text-8xl font-extrabold tracking-tighter leading-[0.9] mb-4 uppercase italic text-white"
          >
            STRATEGIC<br /><span class="text-[#82e637] text-glow"
              >ALCHEMIST</span
            >
          </h1>

          <div class="mb-8 flex items-center gap-3">
            <span
              class="flex items-center gap-2 bg-[#82e637]/10 border border-[#82e637]/30 px-4 py-2 rounded-full"
            >
              <span class="w-2 h-2 bg-[#82e637] rounded-full dot-blink"></span>
              <span
                class="text-[11px] font-bold text-[#82e637] uppercase tracking-[0.2em]"
              >
                Current: Asset Engineer
              </span>
            </span>
          </div>

          <p
            class="max-w-md text-gray-400 text-sm uppercase tracking-widest leading-relaxed border-l-2 border-[#82e637] pl-4"
          >
            Asset Engineer by day, AI Strategist by night. Converting complex
            data into
            <span class="text-white font-bold">Operational Gold</span>.
          </p>
        </div>

        <div
          class="bento-card rounded-[40px] relative group min-h-[400px] md:min-h-[450px]"
        >
          <img
            src="https://lh3.googleusercontent.com/u/0/d/1kQcr0S-z0F1TfAd3mmqjuOYx1nbl814-"
            alt="Azmi Aziz"
            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
          />
          <div
            class="absolute bottom-4 left-4 text-[8px] tracking-[0.4em] text-[#82e637] font-bold bg-black/60 px-2 py-1 rounded"
          >
            IT'S ME
          </div>
        </div>

        <div
          class="md:col-span-4 bento-card py-6 rounded-full marquee-container border-none bg-[#82e637]"
        >
          <div
            class="marquee-content text-black font-extrabold uppercase italic text-2xl"
          >
            <span>STRATEGIC THINKING</span> <span>•</span>
            <span>DATA-DRIVEN MINDSET</span> <span>•</span>
            <span>SYSTEMS THINKING</span> <span>•</span>
            <span>ANALYTICAL PROBLEM-SOLVING</span> <span>•</span>
            <span>BUSINESS ACUMEN</span> <span>•</span>
            <span>COLLABORATIVE LEADERSHIP</span>
          </div>
        </div>

        <div
          class="md:col-span-3 bento-card p-10 rounded-[40px] flex flex-col justify-center border-white/5"
        >
          <h4
            class="text-[10px] font-bold text-[#82e637] uppercase tracking-[0.4em] mb-4"
          >
            // Leadership & Logic
          </h4>
          <p
            class="text-gray-300 text-lg md:text-xl leading-relaxed font-medium italic"
          >
            Informatics graduate from
            <span class="text-white">AMIKOM University Yogyakarta</span>.<br />
            Passionate about
            <span class="text-white">strategic thinking</span>, data-driven
            mindset, systems thinking, analytical problem-solving, business
            acumen, dan collaborative leadership.
          </p>
        </div>

        <div
          class="bento-card p-8 rounded-[40px] flex flex-col justify-between border-emerald-900/30"
        >
          <div
            class="text-[10px] font-bold text-gray-600 uppercase tracking-widest text-center"
          >
            GPA / IPK
          </div>
          <div class="text-center">
            <h2
              class="text-6xl font-bold italic tracking-tighter text-[#82e637]"
            >
              3.75
            </h2>
            <p
              class="text-[11px] text-[#82e637] font-bold uppercase mt-1 tracking-widest text-glow"
            >
              CUMLAUDE
            </p>
            <p class="text-[8px] text-gray-500 uppercase mt-1 tracking-tighter">
              AMIKOM Yogyakarta
            </p>
          </div>
        </div>

        <div class="md:col-span-4 order-2">
          <div class="project-scroll">
            <div
              class="project-item bento-card p-8 rounded-[40px] flex flex-col justify-between min-h-[320px]"
            >
              <div>
                <span
                  class="text-[10px] text-[#82e637] font-bold uppercase tracking-[0.3em]"
                  >Market Intelligence</span
                >
                <h3 class="text-2xl font-bold mt-4 uppercase italic text-white">
                  Stock Analytics
                </h3>
                <p class="text-gray-500 text-xs mt-3 leading-relaxed italic">
                  Automasi prediksi akurat berbasis dua model AI untuk optimasi
                  strategi investasi di BBCA.
                </p>
              </div>
              <a
                href="https://dashboard-skripsi-lstm-tcn.streamlit.app/"
                target="_blank"
                class="text-[10px] font-bold uppercase text-[#82e637] border-b border-[#82e637]/30 self-start pb-1"
                >Live Demo ↗</a
              >
            </div>

            <div
              class="project-item bento-card p-8 rounded-[40px] flex flex-col justify-between min-h-[320px]"
            >
              <div>
                <span
                  class="text-[10px] text-[#82e637] font-bold uppercase tracking-[0.3em]"
                  >Digital Business UI/UX</span
                >
                <h3 class="text-2xl font-bold mt-4 uppercase italic text-white">
                  Dwikarya Platform
                </h3>
                <p class="text-gray-500 text-xs mt-3 leading-relaxed italic">
                  Riset UI/UX untuk digitalisasi UMKM furniture, menghubungkan
                  produk lokal ke pasar modern.
                </p>
              </div>
              <a
                href="https://umkm-dwikarya-uiux.streamlit.app/"
                target="_blank"
                class="text-[10px] font-bold uppercase text-[#82e637] border-b border-[#82e637]/30 self-start pb-1"
                >View Project ↗</a
              >
            </div>

            <div
              class="project-item bento-card p-8 rounded-[40px] flex flex-col justify-between min-h-[320px]"
            >
              <div>
                <span
                  class="text-[10px] text-[#82e637] font-bold uppercase tracking-[0.3em]"
                  >Operational Tool</span
                >
                <h3 class="text-2xl font-bold mt-4 uppercase italic text-white">
                  Smart Predictor
                </h3>
                <p class="text-gray-500 text-xs mt-3 leading-relaxed italic">
                  Automasi pengambilan keputusan berbasis AI untuk optimasi
                  strategi investasi di BBCA.
                </p>
              </div>
              <a
                href="https://appspredictionstock.streamlit.app/"
                target="_blank"
                class="text-[10px] font-bold uppercase text-[#82e637] border-b border-[#82e637]/30 self-start pb-1"
                >Open App ↗</a
              >
            </div>
          </div>
        </div>
        <section
          id="experience"
          class="md:col-span-4 order-1 bento-card p-8 md:p-10 rounded-[40px] border-white/5"
        >
          <div
            class="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-8"
          >
            <div>
              <h4
                class="text-[10px] font-bold text-[#82e637] uppercase tracking-[0.4em] mb-3"
              >
                // Career Log
              </h4>
              <h2
                class="text-3xl md:text-4xl font-bold uppercase italic tracking-tighter"
              >
                Work Experience
              </h2>
            </div>
            <span class="text-[9px] text-gray-600 uppercase tracking-[0.35em]"
              >Oct 2022 — Now</span
            >
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-4">
            <article class="border-l-2 border-[#82e637] pl-5 py-2">
              <div class="flex flex-wrap items-center gap-3 mb-2">
                <span
                  class="text-[10px] text-[#82e637] font-bold uppercase tracking-[0.2em]"
                  >Sep 2026 — Now</span
                >
                <span
                  class="text-[8px] text-black bg-[#82e637] px-2 py-1 rounded-full uppercase font-bold tracking-widest"
                  >Current</span
                >
              </div>
              <h3 class="text-xl font-bold uppercase italic">Asset Engineer</h3>
            </article>

            <article class="border-l border-white/15 pl-5 py-2">
              <span
                class="text-[10px] text-gray-500 font-bold uppercase tracking-[0.2em]"
                >Aug 2026 — Sep 2026</span
              >
              <h3 class="text-xl font-bold uppercase italic mt-2">
                Assistant to Owner & Data Analyst
              </h3>
            </article>

            <article class="border-l border-white/15 pl-5 py-2">
              <span
                class="text-[10px] text-gray-500 font-bold uppercase tracking-[0.2em]"
                >Jan 2025 — Jul 2026</span
              >
              <h3 class="text-xl font-bold uppercase italic mt-2">
                Store Data & Operations Manager
              </h3>
            </article>

            <article class="border-l border-white/15 pl-5 py-2">
              <span
                class="text-[10px] text-gray-500 font-bold uppercase tracking-[0.2em]"
                >Oct 2022 — Dec 2024</span
              >
              <h3 class="text-xl font-bold uppercase italic mt-2">
                Data Entry
              </h3>
            </article>
          </div>
        </section>
      </div>

      <footer class="mt-20 border-t border-white/5 pt-10 text-center">
        <p class="text-[9px] text-gray-700 tracking-[0.5em] uppercase italic">
          Azmi Aziz — Managing the Future // 2026
        </p>
      </footer>
    </main>
  </body>
</html>
"""

st.iframe(html_final, width="stretch", height="content")
