# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

**Or on Windows**, just double-click `run.bat`

### Step 2: Run the Script
```bash
python youtube_refresher.py
```

### Step 3: Enter Your URLs

**Example Session:**
```
YouTube video URL: https://www.youtube.com/watch?v=YOUR_VIDEO
TikTok URL: @creator_username
Use proxy rotation? (y/n): y
Enter '1' to load from file or '2' to enter manually: 1
Enter proxy file path (default: proxies.txt): [press Enter]
Loaded 5 proxies from proxies.txt
Number of browsing sessions: 10
```

Press `y` to start!

💡 **Pro Tip**: Using proxies makes each session appear from a different IP!

---

## 🎯 What It Does

The bot will:
1. ✅ Open Chrome browser
2. ✅ Randomly alternate between YouTube and TikTok
3. ✅ Watch videos with realistic timing (30-90 sec for YouTube, 15-45 sec for TikTok)
4. ✅ Scroll and simulate engagement
5. ✅ Take breaks between sessions
6. ✅ Repeat for your configured number of sessions

---

## 🔐 Proxy Setup (Recommended)

### Why Use Proxies?
- **Different IP each session** = looks like different users
- **Avoid IP bans** from too many requests
- **Better success rate** for view counting

### Quick Proxy Setup

**Option 1: Use proxies.txt file**
1. Open `proxies.txt` in the project folder
2. Add your proxies (one per line):
   ```
   http://proxy1.com:8080
   http://proxy2.com:8080
   192.168.1.1:3128
   ```
3. Save the file
4. When running, choose `y` for proxies, then `1` to load from file

**Option 2: Enter manually**
- Choose `y` for proxies
- Choose `2` for manual entry
- Type each proxy and press Enter
- Press Enter on empty line when done

**Option 3: Skip proxies**
- Choose `n` when prompted
- Uses your real IP (not recommended for many sessions)

### Where to Get Proxies?
- **Free**: Search "free proxy list" (unreliable, for testing only)
- **Paid**: Bright Data, Smartproxy, Oxylabs (reliable, recommended)

---

## 📋 Usage Examples

### YouTube Only
- **YouTube URL:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- **TikTok URL:** *(leave blank)*
- **Sessions:** `10`

### TikTok Creator Profile
- **YouTube URL:** *(leave blank)*
- **TikTok URL:** `@username`
- **Sessions:** `10`

The bot will browse the creator's profile and watch 2-5 random videos!

### Both Platforms (Most Realistic!)
- **YouTube URL:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- **TikTok URL:** `@username`
- **Sessions:** `15`

Bot alternates: ~60% YouTube, ~40% TikTok

---

## ⚙️ How It Works

### YouTube Sessions
1. Opens your video
2. Skips ads automatically
3. Watches 30-90 seconds
4. Random scrolling
5. Sometimes checks comments

### TikTok Sessions
1. Goes to creator profile OR single video
2. If profile: Finds 2-5 videos to watch
3. Watches each for 15-45 seconds
4. Random scrolling and engagement

### Multi-Platform Magic
- Randomly picks YouTube or TikTok each session
- Takes 5-15 second breaks between sessions
- Mimics real human browsing patterns

---

## ⚠️ Important Reminders

- **Educational use only** - This violates platform ToS
- **No guarantees** - Views may still be filtered
- **Use responsibly** - Accounts can be banned
- **Be ethical** - Don't manipulate metrics maliciously

---

## 🔧 Quick Customization

Want to tweak the behavior? Edit `youtube_refresher.py`:

**Line ~56:** Change YouTube watch time
```python
watch_time = random.randint(30, 90)  # Change these numbers!
```

**Line ~249:** Adjust platform ratio
```python
weights = [0.6, 0.4]  # [YouTube %, TikTok %]
```

**Line ~265:** Change break duration
```python
break_time = random.uniform(5, 15)  # Change min/max seconds
```

---

## 💡 Pro Tips

1. **Use both platforms** for most realistic behavior
2. **Start with fewer sessions** (5-10) to test
3. **Longer watch times** = more "legitimate" views
4. **Don't run continuously** - Take breaks between runs
5. **Mix up your URLs** - Don't always use the same video

---

## 🆘 Troubleshooting

**Script won't start?**
```bash
pip install --upgrade undetected-chromedriver selenium
```

**Chrome crashes?**
- Update Google Chrome to latest version
- Restart your computer
- Check internet connection

**Views not counting?**
- Normal! Platforms filter automated views
- Try longer watch times (60-120 seconds)
- Use actual account (not recommended)

---

## 📚 More Info

See `README.md` for detailed documentation!

---

**Ready to experiment? Have fun and stay ethical! 🎉**

