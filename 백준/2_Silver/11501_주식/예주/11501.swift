import Foundation

func sol11501() {
    let input = Int(readLine()!)!
    
//    for _ in 0..<input {
//        let n = Int(readLine()!)!
//        var stocks = readLine()!.split(separator: " ").map { Int($0)! }
//
//        var index = 0
//        var answer = 0
//
//        while index < stocks.count {
//            if stocks.count == 1 {  // 예외케이스 처리
//                break
//            }
//
//            let maxNum = stocks.max()!
//            index = stocks.firstIndex(of: maxNum)!
//
//            for i in 0..<index { //
//                if maxNum > stocks[i] {
//                    answer += maxNum - stocks[i]
//                }
//            }
//
//            if index == stocks.count - 1 {
//                break
//            }
//
//            stocks = Array(stocks[index+1..<stocks.count])
//            index = 0
//        }
//        print(answer)
//    }
    
    for _ in 0..<input {
        _ = Int(readLine()!)!
        let stocks = readLine()!.split(separator: " ").map { Int($0)! }
        
        var maxNum = stocks.last!
        var answer = 0
        
        for index in stride(from: stocks.count - 1, through: 0, by: -1) {
            if maxNum < stocks[index] { // 더 큰값이 들어옴. 판매하지 않고, max값 변경
                maxNum = stocks[index]
            } else if maxNum > stocks[index] { // 판매한다.
                answer += maxNum - stocks[index]
            }
        }
        print(answer)
    }
    
}
//sol11501()
