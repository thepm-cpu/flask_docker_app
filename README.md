# Flask Guestbook App 

A simple guestbook web application built with Flask, styled with CSS, and deployed using Docker, GitHub Actions, and Render.

##  Features
- Submit messages with names
- View messages with timestamps
- Delete individual messages
- Simple UI styling with CSS
- Fully containerized with Docker
- Automatically deployed to Render on code push

---

##  Problems Faced & Solutions

### 1. **Flask Version Error**
**Problem:** `ModuleNotFoundError` or version incompatibility during build.  
**Solution:** Specified `Flask==2.3.3` in `requirements.txt`.

### 2. **404 Not Found on Render**
**Problem:** Homepage gave a 404 error.  
**Cause:** Route was defined after `if __name__ == "__main__":`.  
**Solution:** Moved route definitions above the `if __name__ == "__main__"` block.

### 3. **Message Not Showing**
**Problem:** Message content was not displaying.  
**Solution:** HTML was using `{{ msg.message }}` instead of `{{ msg.content }}`.

### 4. **Docker Port Conflict**
**Problem:** `Bind for 0.0.0.0:5000 failed: port is already allocated`.  
**Solution:** Stopped other Docker containers using `docker ps` + `docker stop`.

### 5. **Database Errors**
**Problem:** Render wouldn’t persist database.  
**Solution:** Used `/tmp/guestbook.db` for compatibility with Render.

### 6. **Double Rendering of Messages**
**Problem:** Messages were showing twice on the page.  
**Solution:** Fixed duplicate rendering in `index.html` by avoiding multiple render blocks and cleaning template.

### 7. **Docker Build Failures**
**Problem:** Couldn’t fetch packages due to DNS failure.  
**Solution:** Restarted Docker, fixed internet configuration.

### 8. **Automatic Deployment**
**Problem:** Had to manually deploy via Render dashboard.  
**Solution:** Integrated GitHub Actions with Render Deploy Hook for CI/CD.

### 9. **Automatic Deployment Faliure**
**Problem** automatic deployment failed.
**Solution** Replaced "main" with "master" as origin 
---

##  Tech Stack

- **Flask**
- **SQLite**
- **Docker**
- **GitHub Actions**
- **Render**

---

## 🛠 Setup

```bash
# Run locally
docker build -t flask-guestbook-app .
docker run -p 5000:5000 flask-guestbook-app
