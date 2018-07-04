'''
Parse Squad Dataset to retrieve (para, question) pairs

'''
import json
import pprint
import numpy as np
# for each topic , for each para , for each question answer make (para, question) pairs
data = json.load(open('dev-v1.1.json'))
topic = data['data']
paraQuestions = [] # stores context (para) question pairs
an = np.zeros(100)
cnt =  0
fid_p = open('dev-para-bio.src','w')
fid_q = open('dev-para-bio.tgt','w')
pp = pprint.PrettyPrinter(indent=4)
for i in range(len(topic)): # iterate over topics
	paras = topic[i]['paragraphs'] # set of all paras + qas within a topic
	for j in range(len(paras)): # iterate over paras in
		para = paras[j]['context'] # get 1 para from dataset
		qas = paras[j]['qas'] # set of question answer pairs in above para

		an[len(qas)] +=1
		for k in range(len(qas)):
			cnt+=1
			# Iam always considering the first answer to be correct one
			ans_index = qas[k]['answers'][0]['answer_start']
			ans_text = qas[k]['answers'][0]['text']
			ans_word_cnt = len(ans_text.split(' '))
			ans_len = len(ans_text)

			ques = qas[k]['question']
			_para = para.split()
			new_para = []
			w_len = 0
			temp_cnt = 0
			for word in _para:
				w_len += len(word) + 1
				if(w_len <= ans_index or temp_cnt == ans_word_cnt):
					new_para.append(word + '￨' + 'O')
				else:
					if(temp_cnt==0) :
						new_para.append(word + '￨' + 'B' )
					else :
						new_para.append(word + '￨' + 'I' )
					temp_cnt+=1
			# print(new_para)
			final_para = ' '.join(new_para)
			fid_q.write(ques + '\n')
			fid_p.write(final_para + '\n')


# print(ans)

fid_p.close()
fid_q.close()
print('Question Para Pairs are Written')
# ff.close()
# ff1.close()
# print(str(cnt) + " question para pairs successfully written")
