from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
moby_dick = open('/Users/mikkel/Downloads/moby_dick.txt',
                 'rt', encoding='utf-8')
fit = vectorizer.fit_transform(moby_dick)
res = fit.todense()
document_idx = vectorizer.vocabulary_['wood']
document_count = sum(res[:, document_idx])
print(document_count)
print(type(document_count))
