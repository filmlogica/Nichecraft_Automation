from pytrends.request import TrendReq

def get_trending_keywords():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        trending = pytrends.trending_searches(pn='united_states')
        return trending[0:5].tolist()
    except Exception as e:
        print(f"⚠️ Could not fetch trending keywords: {e}")
        return ["AI Tools", "Productivity", "Digital Planner", "Workout App", "Sleep Coach"]
