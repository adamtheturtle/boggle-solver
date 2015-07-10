class Tile {
    let column, row: Int
    init(column: Int, row: Int) {
        self.column = column
        self.row = row
    }

    func touching(other: Tile) -> Bool {
        return true
    }
}


func toTiles(word: String) -> [String] {
    return ["A", "B", "C"]
}

func isAvailableRoute(word: String, tile_map: Dictionary<String, [Tile]>) -> Bool {
    return true
    
}

func getTileMap(board: [[String]]) -> Dictionary<String, [Tile]> {
    return ["A": [Tile(column: 1, row: 1)]]
}


func numOccurencesOfASubstring(haystack: String, needle: String) -> Int {
    let haystack_array = Array(haystack.characters)
    let needle_array = Array(needle.characters)
    var count = 0

    for (index, character) in haystack.characters.enumerate() {
        var substring_of_needle_length = Array(haystack_array[0..<needle_array.count])
        var is_correct = substring_of_needle_length == needle_array
        if is_correct {
            count++
        }
    }
    return count
}

func tilesAvailable(word: String, tile_map: Dictionary<String, [Tile]>) -> Bool {
    let tiles = toTiles(word)
    for tile in tiles {
        let occurences = numOccurencesOfASubstring(word, needle: tile)
        var positions = tile_map[tile]
        if positions == nil {
            return false
        }

        let num_positions = positions?.count
        return occurences <= num_positions
    }

    return true
}

func isValidWord(word: String, tile_map: Dictionary<String, [Tile]>) -> Bool {
    if word.characters.count > 2 {
        if tilesAvailable(word, tile_map: tile_map) {
            return isAvailableRoute(word, tile_map: tile_map)
        }
    }
    return false
}

func listWords(board: [[String]], word_list: Set<String>) -> Set<String> {
    let tile_map = getTileMap(board)
    var words = Set<String>()
    for word in word_list {
        if isValidWord(word, tile_map: tile_map) {
            words.insert(word.uppercaseString)
        }
    }

    return words
}

let my_board : [[String]] = [
    ["A", "B"],
    ["C", "D"],
]

let word_list : Set<String> = Set(arrayLiteral: "abc", "ab", "abd", "foo")

//listWords(my_board, word_list: word_list)

numOccurencesOfASubstring("abcabc", needle: "ab")
