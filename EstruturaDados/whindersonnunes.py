numero_de_videos = int(input())
vetor_views = []
videos_viral = 0
videos_nao_viral = 0

for i in range(numero_de_videos):
    views = int(input())
    vetor_views.append(views)

for i in range(numero_de_videos):
    if vetor_views[i] >= 10000000:
        videos_viral += 1
    if vetor_views[i] < 10000000:
        videos_nao_viral += 1

print(f"{videos_viral} video(s) com mais de 10M de views")
print(f"{videos_nao_viral} video(s) com menos de 10M de views")