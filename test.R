

message = "the quickfffffffffff brown fox jumps over the lazy dog"

N = 10

words = strsplit(message, " ")[[1]]

current = NULL
current_len = 0
chunk = ""

for (word in words) {
    if(stringr::str_length(word) >= N){
        current <- append(current, chunk)
        current <- append(current, word)
        current_len <- 0
        chunk <- ""
        next
    }
    if(stringr::str_length(word) +  current_len >= N){
        current <- append(current,  chunk)
        current_len <- 0
        chunk <- word
    } else {
        chunk <- paste(chunk, word)
        current_len <- stringr::str_length(chunk)
    }

}

current <- append(current,  chunk)
print(current)