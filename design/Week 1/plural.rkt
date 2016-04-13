;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname plural) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; String -> String
;; pluralises a word by adding "s" at the end

(check-expect (plural "horse")"horses")
(check-expect (plural "bee")"bees")
(check-expect (plural "fire hidrent")"fire hidrents")

;(define (plural word) "s")

;(define (plural word)
;  (... word))

(define (plural word)
  (string-append word "s"))