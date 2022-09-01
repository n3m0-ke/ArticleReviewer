from django.shortcuts import render
from kurdish import ku

def index(request):
	context = {
		"title": "Revisor Page",
	}	
	return render(request, 'revisor.html', context=context)

# Create your views here.
def rewrite(request):
	context = {
		"title": "Rewrite Page",
	}
	if request.method == "POST":
		counter = 0
		paragraphs = []
		num_words = 0
		while True:
			name="paragraph"+str(counter)
			if name in request.POST:
				eng_string = ku.Hemwar().transliterate(request.POST[name])
				num_words+= len(eng_string.split())
				paragraphs.append(request.POST[name])
			else:
				break
			counter+=1
		context["num_words"] = num_words
		article = "\n".join(paragraphs)
		
		words_in_article = article.split()
		word_dict = dict()

		for word in words_in_article:
			checked_words = []
			if not(word in checked_words):
				num_occurrences = words_in_article.count(word)
				checked_words.append(word)

				if num_occurrences > 1:
					word_dict[word] = num_occurrences
				
		# article = "" + article
		print(word_dict)
		context["article"] = article
		context["word_dict"] = word_dict
	return render(request, 'rewrite.html', context=context)


# (ئەسیری بسکی ئاڵۆزی کچە کوردێکی نەشمیلم، تەماشا کەن چ سەیرێکە بەدەستی دیلەوە دیلم. (هێمن موکریانی

def preview(request):
	context = {
		"title": "Preview Page",
	}
	if request.method == "POST":
		string = request.POST['article'].strip()
		new_string = ku.Hemwar().transliterate(string)
		context["num_words"] = len(new_string.split())
		paragraphs = string.split('.')
		paragraphs.remove('')		
		print(paragraphs)
		paragraph_dict = dict()
		counter = 0
		for paragraph in paragraphs:
			name = "paragraph"+str(counter)
			paragraph_dict[name] = paragraph
			counter+=1
		context['paragraphs'] = paragraph_dict
	return render(request, 'preview.html', context=context)