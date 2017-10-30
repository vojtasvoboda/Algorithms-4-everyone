#lang racket

(define (quick-sort ls)
  (if (empty? ls)
    ls
    (letrec ([pivot (first ls)]
             [left (filter (lambda (x) (<= x pivot)) (rest ls))]
             [right (filter (lambda (x) (> x pivot)) (rest ls))])
            (append (quick-sort left) (list pivot) (quick-sort right)))))

(quick-sort '(42 15 4 8 23 16))
