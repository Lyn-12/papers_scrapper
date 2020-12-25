import csv
from scholarly import scholarly, ProxyGenerator
import json
import psycopg2
import io

# authors = []
# authors.append('Byung Kyu Kim') this one is done

authors = [
    # 'Byung Kyu Kim' done 
    # 'Andrea Toldy', not found
    # 'Ahmad Reza Bahramian', not found
    # 'Jens Gaitzsch', not found
    # 'Jan Feijen',  done
    #'PWM Blom', done
    #'Katharina Landfester', not found
    # 'Kurt Kremer', done partition 3
    # 'Qiang Fu' done partition 5
    # 'Carlo Dallapiccola', done partition 6
    # 'Francisco Matorras', done partiton 7
    # 'Haijun Yang', done
    # 'Martin Grunewald', done
    # 'Robert M Roser', done partition 8
    # 'Tamleek Ali Tanveer', done partition 9
    #'HR Rao' ,
    #'stefan thor smith' ,
    #'Leroy Hood' ,
    #'Bernhard Schölkopf' ,
    #'Ana Valeria Barros Castro' ,
    #'Larry R Squire' 
    #'Michael H Jones' 
    #'Henning Hermjakob' 
    #'James C. Bezdek' 
    #'Eric Finkelstein' 
    #'Petre (Peter) Stoica' 
    #'Edmond K Kabagambe' 
    #'Stuart Kauffman' 
    #'Graesser' 
    #'Mark Handley' 
    #'Michael Busch' 
    #'Michael Busch' 

    ## mehdi authors down ⬇️
    #'Prof. Dr. Hameed Ullah Khan' Done 1001
    #'Luis A. Nunes Amaral' Done 1002
    #'Nebojsa Nakicenovic' Done 1003
    #'Nikolaus Rajewsky' Done 1004
    #'Jeffrey Cohn' Done 1005 
    #'Giovanni Santin' Done 1006 
    #'Gerard Muyzer' Done 1007
    #'JP Casas' Done 1008 
    #'Andrzej Cichocki' Done 1009
    #'Michael J. Black' Done 1010
    #'Simon B. Eickhoff' Done 1011
    #'James Randerson' Done 1012
    #'Harry J. Wang' Done 1013
    #'Sheldon Ross' Done 1014 
    #'Stuart C Gordon'  Done 1015
    #'Peter Cox' Done 1016 
    'Fred Hirsch' 
    #'Bev Law' 

    
]

csv_columns = ['id','abstract','author','cites','cites_id','journal','number','pages','publisher','title','url','volume','year','citation_link' , 'id_citations']
partition_str = input("Enter the partition number (mehdi should start from 1000 eg 1001,1002,1003 ...etc): ")
partition_number =int(partition_str)
counter = partition_number * 1000
# counter=5000
partition= str(round(counter/1000) ) 
csv_file = "datasets/articles_part"+partition_str+".csv"
for author_name in authors:
    try:
        with io.open(csv_file, "w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
            writer.writeheader()

            # Retrieve the author's data, fill-in, and print
            search_query = scholarly.search_author(author_name)
            author = next(search_query).fill()

            # Take a closer look at the first publication
            pubs = author.publications
            dict_data = []
            
            for idx,pub in enumerate(pubs):
                pub_filled = pub.fill()
                print(pub_filled)
                pub_filled.bib['id']= idx+counter

                if hasattr(pub_filled, 'citations_link'):
                    pub_filled.bib['citation_link']= pub_filled.citations_link

                if hasattr(pub_filled, 'id_citations'):
                    pub_filled.bib['id_citations']= pub_filled.id_citations

                dict_data.append(pub_filled.bib)
                writer.writerow(pub_filled.bib)
                
                
    except IOError:
        print("I/O error")
        
    

  
    
