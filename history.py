import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName', 'en')

CountryName = input()

page_py = wiki_wiki.page(CountryName)

print("Title: %s" % page_py.title)
    

print("Summary: %s" % page_py.summary[0:1000])