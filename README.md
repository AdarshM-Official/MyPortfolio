# Adarsh M — Developer Portfolio

Modern, minimalist, and responsive developer portfolio website for **Adarsh M**, Python/Django Developer focused on AI-integrated web applications.

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
