import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print "[*] Creating crawler project : {0}".format(directory)
        os.makedirs(directory)
    else:
        print "[*] Crawler project already exists. continuing.."

def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url,'w')
        print "[*] Creating URLs Queue file."
    if not os.path.isfile(crawled):
        write_file(crawled, '','w')
        print "[*] Creating Crawled URLs file."


def write_file(file_name, data, mode):
    with open(file_name, mode) as outfile:
        outfile.write(data+'\n')


def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as outfile:
        for line in outfile:
            results.add(line.strip())
    return results

def set_to_file(links,file):
    write_file(file,'','w')
    for link in sorted(links):
        write_file(file,link,'a')


