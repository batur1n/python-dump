class Student:

    conf = {'exam_max' : 30, 'lab_max' : 7, 'lab_num' : 10, 'k' : 0.61 }
    labs = [0] * conf.get('lab_num')
    exam = int()
    passed = bool()
    
    def student(name, conf)


    def make_lab(m, n):
        if n <= len(labs):
            labs[n] = m
        elif n == None:
            for i in labs:
                if i == 0:
                    labs[i] = m
                    break
                else:
                    print('All labs are completed!')

    def make_exam(m):
        if m in range(0,30) and m > 0:
            exam = m
        elif m > 30:
            exam = 30

    def is_cerified():
        result = sum(labs) + exam
        if result/100 >= conf.get('k')
            passed = True
        else:
            passed = False
        return (result, passed)

oleg
