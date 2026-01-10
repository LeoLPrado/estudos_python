seconds = int(input())

hours = int(seconds/ 3600)
minutes = int(seconds / 60)
N = seconds - ((minutes * 60) + (hours * 60))

print(f"{hours}:{minutes}:{N}")