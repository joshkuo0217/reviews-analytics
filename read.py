data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: #%是用來求餘數
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言含有good')

print(good[0])

godness = [1 for d in data if 'good' in d]

print(godness)

#快寫: good = [d for d in data if 'good' in d]...為23-26
#d 也可以裝布林值或者其他數字來代表之

bad = ['bad' in d for d in data] # 'bad' in d 變成布林值判斷

print(bad)