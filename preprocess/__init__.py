import os


def get_all_sentences(root_dir="dataset"):
    """Get all sentence pairs from given directory
    
    Keyword Arguments:
        root_dir {str} -- [Root directory contianing dataset files] (default: {"dataset"})
    
    Returns:
        [dict] -- [amharic sentence , english sentence pairs]
    """
    output = dict()

    for f in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, f)):
            for f2 in os.listdir(os.path.join(root_dir, f)):
                current_amharic_filename = None
                current_english_filename = None
                if f2.startswith("amharic"):
                    current_amharic_filename = os.path.join(root_dir, f, f2)
                    current_english_filename = current_amharic_filename.replace("amharic", "english")
                elif f2.startswith("am."):
                    current_amharic_filename = os.path.join(root_dir, f, f2)
                    current_english_filename = current_amharic_filename.replace("am.", "en.")
                elif f2.startswith("new-am"):
                    current_amharic_filename = os.path.join(root_dir, f, f2)
                    current_english_filename = current_amharic_filename.replace("am", "en")
                if current_amharic_filename is not None and current_english_filename is not None:
                    current_amharic_sents = []
                    current_english_sents = []
                    with open(os.path.join(root_dir, f, f2)) as amharic_file:
                        for line in amharic_file.readlines():
                            current_amharic_sents.append(line.replace("\n",""))
                    with open(os.path.join(root_dir, f, f2.replace("amharic","english"))) as english_file:
                        for line in english_file.readlines():
                            current_english_sents.append(line.replace("\n",""))
                    
                    assert len(current_amharic_sents) == len(current_english_sents),"the sentences should be equal numbers, file::"+os.path.join(root_dir, f,f2)
                    for i in range(len(current_amharic_sents)):
                        output[current_english_sents[i]] = current_amharic_sents[i]
            print("processed", os.path.join(root_dir,f),"directory")
        else:
            if f.startswith("amharic"):
                current_amharic_filename = os.path.join(root_dir, f)
                current_english_filename = current_amharic_filename.replace("amharic", "english")
            elif f.startswith("am."):
                current_amharic_filename = os.path.join(root_dir, f)
                current_english_filename = current_amharic_filename.replace("am.", "en.")
            elif f.startswith("new-am"):
                current_amharic_filename = os.path.join(root_dir, f)
                current_english_filename = current_amharic_filename.replace("am", "en")
            if current_amharic_filename is not None and current_english_filename is not None:
                current_amharic_sents = []
                current_english_sents = []
                with open(os.path.join(root_dir, f)) as amharic_file:
                    for line in amharic_file.readlines():
                        current_amharic_sents.append(line.replace("\n",""))
                with open(os.path.join(root_dir, f.replace("amharic","english"))) as english_file:
                    for line in english_file.readlines():
                        current_english_sents.append(line.replace("\n",""))
                
                assert len(current_amharic_sents) == len(current_english_sents),"the sentences should be equal numbers, file::"+os.path.join(root_dir, f)
                for i in range(len(current_amharic_sents)):
                    output[current_english_sents[i]] = current_amharic_sents[i]
            # print(current_amharic_sents[0])
            # print(current_english_sents[0])
            # os._exit(0)

    return output