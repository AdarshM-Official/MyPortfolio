# Adarsh M — Developer Portfolio

Modern, minimalist, and responsive developer portfolio website for **Adarsh M**, Python/Django Developer focused on AI-integrated web applications.

---

## 📄 Adding Your Resume PDF
Place your resume PDF file here:
```text
assets/docs/resume.pdf
```
All **"Download Resume"** buttons in the header, hero section, and mobile drawer are pre-linked to directly download or view `assets/docs/resume.pdf` as `Adarsh_M_Resume.pdf`.

---

## 📸 Adding Your Photo
A photo frame with ambient animations is integrated in the Hero section:
1. Save your photo as **`profile.jpg`** (or `.png` / `.webp`).
2. Place it into the folder:
   ```text
   assets/images/profile.jpg
   ```
3. If no photo is found yet, it automatically falls back gracefully to [`profile-placeholder.svg`](file:///d:/Adarsh/Portfolio/Potfolio/assets/images/profile-placeholder.svg).

---

## ✨ Design & Animation Features Added
- **Profile Presentation**: Floating glassmorphism card with ambient glow aura, floating badges (*"Python/Django"*, *"Applied AI & LLMs"*, *"MCA '26"*), and smooth hover zoom.
- **Dynamic Typing Subtitle**: Cycles through *"Python / Django Developer"*, *"Applied AI & ML Engineer"*, *"Full-Stack SaaS Architect"*, and *"MCA Candidate '26"*.
- **Mouse Spotlight Cursor Effect**: Subtle radial glow following mouse movement on desktop screens.
- **Scroll Reveal Transitions**: Smooth intersection observer animations as each section slides into view.
- **3D Interactive Tilt Cards**: Micro-elevation and glow borders when hovering over project cards, certifications, and experience entries.
- **Project Filter Tabs**: Seamless instant filtering between **All**, **AI / ML**, and **Full-Stack** projects.

---

## 🛠️ Featured Engineering Projects Included
1. **MediConnect AI** — Smart Healthcare Discovery & Emergency Coordination Platform (Python 3.12, Django 5.2, Leaflet.js, Haversine, Groq Voice AI, 5-Role RBAC, Concurrency Guards, 57+ Tests).
2. **LegalAI** — Legal Assistant & Document Intelligence Engine (Django, ChromaDB, Sentence-Transformers `all-MiniLM-L6-v2`, Groq Cloud LLM, PyPDF, Contract Parsing).
3. **MediReport AI** — Clinical Document Multimodal Extraction & Health Analytics (Django, Gemini API, LangChain, OpenCV, ReportLab).
4. **BookingCloud** — Multi-Tenant SaaS Subdomain Booking Platform with Groq Voice Assistant.
5. **Multi-College Personalised Management Platform** — Education Cloud Ops & Timetabling Solver.
6. **LearnLoop – AI Career Compass** — Machine Learning Career Path Recommendation System ([Live Demo](https://learnloop-1ywm.onrender.com/) | [GitHub](https://github.com/Nekha024/LearnLoop)).
7. **Farmie** — Agricultural Assistance Web Service (PostgreSQL, PHP, Admin Panel).

---

## 📬 Contact Form Direct Email Delivery (Web3Forms)
The contact form has been upgraded with asynchronous direct background submission:
1. Go to [web3forms.com](https://web3forms.com/) and enter your email (`adarshm.off@gmail.com`).
2. Copy the free access key sent to your inbox.
3. In [`index.html`](file:///d:/Adarsh/Portfolio/Potfolio/index.html) (inside `handleContactSubmit`), replace `'YOUR_ACCESS_KEY_HERE'` with your key:
   ```javascript
   access_key: 'YOUR_ACCESS_KEY_HERE'
   ```
*If left as is, or if a user has connection issues, the form automatically falls back to opening a pre-filled email draft to `adarshm.off@gmail.com`.*

---

## 🚀 How to Host on Render (Free & Instant)

### Option 1: Render Static Site (Recommended)

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Add photo frame and modern interactive animations"
   git branch -M main
   git remote add origin https://github.com/AdarshM-Official/<your-portfolio-repo-name>.git
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to [dashboard.render.com](https://dashboard.render.com/)
   - Click **New +** > **Static Site**
   - Connect your GitHub repository
   - Settings:
     - **Name**: `adarsh-m-portfolio`
     - **Branch**: `main`
     - **Build Command**: *(leave empty)*
     - **Publish Directory**: `.`
   - Click **Create Static Site**

Render will automatically deploy and provide a free SSL-secured URL.
