(define closest (lambda (lst total sublength target)
                     (cond
                       ((null? lst) (if (<= total target) 0 -1))
                      
                       
                       ((< (+ (car lst) (closest (cdr lst) (- total (car lst)) (+ 1 sublength) target))
                           (- (car lst) (closest (cdr lst) total sublength target)))
                        (+ (car lst) (closest (cdr lst) (- total (car lst)) (+ 1 sublength) target)))
                       (else (- (car lst) (closest (cdr lst) total sublength target))))))
