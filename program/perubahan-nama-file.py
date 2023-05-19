class renameQuery():
    for x in id_list:
        for y in range(1, length_int, 3):
            if x == split_data_query_text[y]:
                src_path = query_save_path + '/' + x + '/' + split_data_query_text[y-1]
                dst_path = rename_query_save_path + '/' + x
                if not os.path.isdir(dst_path):
                        os.mkdir(dst_path)
                
                if int(split_data_query_text[y]) > 0 and int(split_data_query_text[y]) < 10:
                        new_id = '0000' + split_data_query_text[y]
                elif int(split_data_query_text[y]) >=10 and int(split_data_query_text[y]) < 100:
                        new_id = '000' + split_data_query_text[y]
                elif int(split_data_query_text[y]) >=100 and int(split_data_query_text[y]) <1000:
                        new_id = '00' + split_data_query_text[y]
                elif int(split_data_query_text[y]) >=1000:
                        new_id = '0' + split_data_query_text[y]
                if int(split_data_query_text[y+1]) > 0 and int(split_data_query_text[y+1]) <10:
                        new_cam = '000' + split_data_query_text[y+1]
                elif int(split_data_query_text[y+1]) >=10 and int(split_data_query_text[y+1]) <100:
                        new_cam = '00' + split_data_query_text[y+1]
                elif int(split_data_query_text[y+1]) >=100 and int(split_data_query_text[y+1]) <1000:
                        new_cam = '0' + split_data_query_text[y+1]
                
                old_name = split_data_query_text[y-1]
                copyfile(src_path, dst_path + '/' + old_name)
                new_name = new_id + '_' + new_cam + '_' + str(image_count_per_id) + '.jpg'
                os.rename(dst_path + '/' + old_name, dst_path + '/' + new_name)
                print(new_name)
                image_count_per_id = image_count_per_id + 1
            else:
                continue
        image_count_per_id = 0