class Tile {
    let column, row: Int
    init(column: Int, row: Int) {
        self.column = column
        self.row = row
    }

    func touching(other: Tile) -> Bool {
        let horizontally_adjacent = abs(self.column - other.column) <= 1
        let vertically_adjacent = abs(self.row - other.row) <= 1
        return horizontally_adjacent && vertically_adjacent
    }
}


func toTiles(word: String) -> [String] {
    var result : [String] = []
    for (index, character) in word.characters.enumerate() {
        if index != 0 && character == "U" && Array(word.characters)[index - 1] == "Q" {
            continue
        } else {
            if character == "Q" {
                result.append("QU")
            } else {
                result.append(String(character))
            }
        }
    }

    return result
}

func isAvailableRoute(word: String, tile_map: Dictionary<String, [Tile]>) -> Bool {
    var routes : [[Tile]] = []
    let tiles = toTiles(word)
    let word_length = word.characters.count
    for letter in tiles {
        let positions = tile_map[letter]
        var new_routes : [[Tile]] = []

//        for route in routes {
//            let num_postions = positions?.count
//            // TODO loop through positions
//            var position = positions?.first
//            var touching = position?.touching(route[-1])
//            if touching == true {
//                continue
//            }
//            if route.last?.touching(position) {
////                TODO if not position in route
//                route.contains(position)
//                if true {
//                    var new_route : [Tile] = route
//                    
//                }
//            }
//            
//        }
        
    }
    return true
    
}

func getTileMap(board: [[String]]) -> Dictionary<String, [Tile]> {
    var mapping = Dictionary<String, [Tile]>()
    for (row_index, row) in board.enumerate() {
        for (column_index, piece) in row.enumerate() {
            let key = piece.uppercaseString
            let tile = Tile(column: column_index, row: row_index)
            if (mapping[key]?.count != nil) {
                mapping[key]?.append(tile)
            } else {
                mapping[key] = [tile]
            }
        }
    }

    return mapping
}


func numOccurencesOfASubstring(haystack: String, needle: String) -> Int {
    let haystack_array = Array(haystack.characters)
    let needle_array = Array(needle.characters)
    var count : Int = 0

    for (index, _) in haystack.characters.enumerate() {
        let end_point: Int = index + needle_array.count
        if end_point > haystack_array.count {
            return count
        }
        let substring_of_needle_length = Array(haystack_array[index..<end_point])
        if substring_of_needle_length == needle_array {
            count++
        }
    }

    return count
}

func tilesAvailable(word: String, tile_map: Dictionary<String, [Tile]>) -> Bool {
    let tiles : [String] = toTiles(word)
    for tile in tiles {
        let occurences : Int = numOccurencesOfASubstring(word, needle: tile)
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

listWords(my_board, word_list: word_list)

numOccurencesOfASubstring("abcabc", needle: "abc")
numOccurencesOfASubstring("abcabc", needle: "abd")
numOccurencesOfASubstring("abcabc", needle: "abca")
numOccurencesOfASubstring("abcabc", needle: "ab")

toTiles("UADAMQUA")
var route = ["A", "B"]
route.last
