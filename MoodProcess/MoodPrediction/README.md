# Mood Process-Mood Prediction

dataset format:

[title, description, importancy, difficulty, comment, time(week), time(hour), time(last period)]

[str, str, float(0-1), float(0-1), int, int, float, float]

comment = [1:life, 2:study, 3:work, 4: entertainment, 5:special, 6:other]

time(week)=int(1,2,3,4,5,6,7)
time(hour)=float(1-24)


please download "glove.6B.50d.txt" and put it in "MoodPrediction->MoodPrediction->datasets"
https://drive.google.com/file/d/1mpQoD3H7UTakoiH9istGThwP7gdAvTrh/view?usp=sharing
