from textblob import TextBlob
import webbrowser

# --- Sentiment Analysis ---
message = input("Type your message: ").strip()

if not message:
    print("⚠️ You didn't type anything.")
else:
    blob = TextBlob(message)
    sentiment = blob.sentiment.polarity

    if sentiment < -0.3:
        print("😔 I'm really sorry you're feeling this way. Things will get better.")
    elif -0.3 <= sentiment < 0:
        print("😕 Sounds a bit off. Hope everything is okay.")
    elif sentiment == 0:
        print("😐 Neutral vibes. Got it.")
    elif 0 < sentiment <= 0.3:
        print("🙂 Nice to hear that!")
    else:
        print("😎😍 That's awesome! Keep it up!")

# --- Website Opener ---
site = input("\nWhich site do you want to open? (youtube / wikipedia / google): ").strip().lower()

allowed_sites = ["youtube", "wikipedia", "google"]

if site in allowed_sites:
    url = f"https://www.{site}.com"
    webbrowser.open(url)
    print(f"🌐 Opening {site.capitalize()}...")
else:
    print("❌ Sorry, this site is not supported.")
