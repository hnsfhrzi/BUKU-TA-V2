class splittingDataset():
    for x in range(0, 5660):
        if not os.path.isdir(rename_train_save_path + '/' + str(x)):
            continue
        else:
            print(x)
            src_path = rename_train_save_path + '/' + str(x) + '/'
            dst_path = rename_val_save_path + '/' + str(x)
            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)

            file_list = os.listdir(src_path)
            print(file_list)

            if len(file_list) < 2:
                continue
            else:
                random_image = random.choice(file_list)
                move(os.path.join(src_path, random_image), os.path.join(dst_path, random_image))