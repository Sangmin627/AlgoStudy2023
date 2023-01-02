import Foundation

let namePool: [String] = ["ari", "ross", "ri", "a"]
var nameIdx = 0

var lastNum = 0
var lastPadding = 0

func suggestedNickName() -> String? {
    while namePool[nameIdx].count
            + String(lastNum).count
            + lastPadding > 5
            && nameIdx < namePool.count {
        if lastPadding != 0 {
            lastPadding = 0
            lastNum += 1
        }
        else {
            lastNum = 0
            nameIdx += 1
        }
    }

    guard nameIdx < namePool.count else {
        return nil
    }
    
    var padding = ""
    (0..<lastPadding).forEach { _ in
        padding += "0"
    }
    let ret = namePool[nameIdx] + padding + String(lastNum)
    lastPadding += 1
    
    return ret
}

let result = suggestedNickName()
print(result)
