import cv2
import numpy as np
from sklearn import preprocessing, train_test_split, svm

generated_filepath = '../Generated/'
n_signs = 29
y_base = np.zeros((n_signs,), dtype=np.int)
row_count = 0;
for sign_count in range(0:n_signs)
	inputdir = generated_filepath + sign_count + '/'
	y_sign = y_base
	y_sign(sign_count) = 1;
	for image in os.listdir(inputdir)
		img_matrix = imread(image)
		img_array = img_matrix.ravel()
		y_matrix(row_count,:) = y_sign
		x_matrix(row_count,:) = img_array
		row_count++
#full_matrix = np.concatenate((x_matrix,y_matrix.T), axis=1)
#full_matrix = np.random.shuffle(full_matrix)

#[rows, columns] = np.shape(full_matrix)
#x_matrix = full_matrix(:,0:columns-n_signs-1)
#y_matrix = full_matrix(:,columns-n_signs:columns-1)

X_train, X_test, Y_train, Y_test = train_test_split(x_matrix,y_matrix,test_size=0.33)

clf = svm.SVC()
clf.fit(X_train,Y_train)

accuracy = clf.score(X_test,Y_test)



