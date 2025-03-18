import sklearn
datasets = sklearn.datasets.fetch_california_housing()

#1. 문제데이터 x_data 정답데이터 y_data를 분리하시오
x_data = datasets["data"]
y_data = datasets["target"]
print(x_data.shape)
print(y_data.shape)
#2. feature_names 를 feature 변수로 분리하여 필드별 문제파일의 특성을 기재하시오
feature = datasets["feature_names"]
print(feature)
#['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
# MedInc- 평균 그룹의 중간 소득
# HouseAge- 평균 주택 년한
# AveRooms- 가구당 평균방의 갯수
# AveBedrms- 가구당 평균 침실수
# Population- 평균 인구수
# AveOccup- 평균 인원수
# Latitude- 위도
# Longitude- 경도
print(datasets["target_names"])#가격
