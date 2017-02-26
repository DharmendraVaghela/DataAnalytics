import json

def digest_businesses():
    business_type_dict={}
    decoder=json.JSONDecoder()
    category_set=set()
    fbusiness=open('../Dataset/business.json','r')
    for business in fbusiness:
        business_attr=decoder.decode(business)
        business_id=business_attr['business_id']
        business_categories=business_attr['categories']
        business_type_dict[business_id]=business_categories
        for category in business_categories:
            category_set.add(category)
    fbusiness.close()
    return business_type_dict,category_set

def get_file_list(categories):
    files_dict={}
    for category in categories:
        files_dict[category]=open('../CategorizedJSON/category_%s.json'%category.replace(' ','_').replace('/','_'),'w')
    return files_dict

def close_files(files_dict):
    for file_l in files_dict.keys():
        files_dict[file_l].close()

def process_reviews(business_dict,files_dict):
    freview=open('../Dataset/review.json','r')
    decoder=json.JSONDecoder()
    for review_s in freview:
        review_attr=decoder.decode(review_s)
        review_business=review_attr['business_id']
        business_categories=business_dict[review_business]
        for category in business_categories:
            files_dict[category].write(review_s+'\n')
    freview.close()

def main():
    businesses,categories=digest_businesses()
    files=get_file_list(categories)
    process_reviews(businesses,files)
    close_files(files)
    

if __name__ == '__main__':
    main() 
