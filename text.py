from google import genai

client = genai.Client(api_key="AIzaSyAzfRGFpTH27RnYn5-BKnuko-C14sLG5UM")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Make a (am i the asshole) under 100 words, paragraph"
)
f = open("story.txt", "x")

for x in response.text:
    f.write(x)

