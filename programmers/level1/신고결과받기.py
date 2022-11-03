def solution(id_list, reports, k):
	dic_report = {id: [] for id in id_list}
	answer = [0] * len(id_list)
	for report in set(reports):
		report = report.split(' ')
		dic_report[report[1]].append(report[0])
	for key, value in dic_report.items():
		if len(value) >= k:
			for v in value:
				answer[id_list.index(v)] += 1
	return answer


###q
# stop = []
    # answer = [0] * len(id_list)
    # dicReports = {id: [] for id in id_list} ##dictionary로 만듬
    # for i in set(reports):
    #     report = i.split(' ') ##쪼갬
    #     stop.append(report[1])
    #     dicReports[report[0]].append(report[1]) ##dictionary에 추가함
    # print(dicReports)
    # stop = set([i for i in stop if stop.count(i) >= k])

    # for key, value in dicReports.items():
    #     for s in stop:
    #         if s in value:
    #             answer[id_list.index(key)] += 1

####################내가 했던 코드
# import pandas as pd

# def solution(id_list, report, k):	
# 	df = pd.DataFrame(report)
# 	df['sender'] = df[0].str.split().str[0]
# 	df['reporting'] = df[0].str.split().str[1]
# 	df = df.drop(df.columns[[0]], axis=1)
# 	df = df.drop_duplicates()
# 	report_cnt = []
# 	result = []
# 	for name in id_list:
# 		report_cnt.append(int(len(df.loc[df['reporting'] == name]) / 2))
# 	cnt = 0
# 	for name in id_list:
# 		for i in range(len(report_cnt)):
# 			if report_cnt[i] >= 1:
# 				if (len(df.loc[(df['sender'] == name) & (df['reporting'] == id_list[i])]) > 0):
# 					cnt += 1
# 					continue
# 		result.append(cnt)
# 		cnt = 0

if __name__ == "__main__":
	id_list = ["muzi", "frodo", "apeach", "neo"]
	report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
	# id_list = ["con", "ryan"]
	# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
	k = 2
	print(solution(id_list, report, k))