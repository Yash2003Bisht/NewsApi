from website import webApp
from flask import jsonify
from website.models import NewsData
app = webApp()

@app.route("/")
def index():
    """main function which return news data in json formate"""
    return "<h3>Click <a href='api/news-data'>here</a> to get api data</h3>"

@app.route("/api/news-data")
def news_data():
    """main function which return news data in json formate"""
    data = {"news": []}
    news = NewsData.query.all()
    for new_data in news:
        title_en = new_data.title_en
        desc_en = new_data.desc_en
        title_fr = new_data.title_fr
        desc_fr = new_data.desc_fr
        timestamp = new_data.timestamp
        image_url = new_data.image_url

        data["news"].append(
            {"title_en": title_en, "desc_en": desc_en, "title_fr": title_fr, "desc_fr": desc_fr, "timestamp": timestamp,
             "image_url": image_url})
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
