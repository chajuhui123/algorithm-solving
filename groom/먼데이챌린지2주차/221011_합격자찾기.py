# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# t: 시험의 갯수 
t = int(input())

for _ in range(t):
	n = int(input()) # 응시 인원의 수
	exams = list(map(int, input().strip().split(" ")))
	
	exam_average = sum(exams) / n # 시험 성적 평균
	count = len([exam for exam in exams if exam >= exam_average])
	
	print('%d/%d' %(count, n))