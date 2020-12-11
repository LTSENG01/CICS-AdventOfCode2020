(defparameter *input*
  (with-open-file (in "10in")
    (sort
     (loop for line = (read-line in nil)
           while line
           collect (parse-integer line))
     #'<)))

(defun part-1 (input)
  (loop for a on (cons 0 input)
        with three-jolts = 0
        and one-jolt = 0
        do (case (if (cadr a) (- (cadr a) (car a)) 3)
             ((3) (incf three-jolts))
             ((1) (incf one-jolt))
             (otherwise t))
        finally (return (* three-jolts one-jolt))))
(format t "~a~%" (part-1 *input*))

(defun part-2 (input)
  (let ((memo (make-hash-table)))
    (labels ((combinations (src tgt next)
               (cond ((= src tgt) 1)
                     ((gethash src memo) (gethash src memo))
                     (t
                      (setf (gethash src memo)
                            (let ((combos
                                    (append
                                     (if (<= (- tgt src) 3) (list tgt) nil)
                                     (loop for a in next
                                           while (<= (- a src) 3) collect a))))
                              (apply #'+ 
                                     (mapcar (lambda (c)
                                               (funcall #'combinations c tgt
                                                        (remove-if
                                                         (lambda (e) (<= e c))
                                                         next)))
                                             combos))))))))
      (funcall #'combinations 0 (+ 3 (car (last input))) input))))
(format t "~a~%" (part-2 *input*))
