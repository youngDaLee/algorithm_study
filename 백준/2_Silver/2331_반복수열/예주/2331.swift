/*
 1. arr의 마지막 요소를 꺼내서 각자리수에 p를 곱한 거 계산
  - 해당 값(m)이 arr에 없으면 m을 append
  - 해당 값(m)이 arr안에 존재한다면, arr의 인덱스 0~m의 인덱스까지 삭제
     - arr 길이 출력
 */

func sol2331() {
    let input = readLine()!.split(separator: " ")
    var arr: [String] = [String(input[0])]
    let p = Int(input[1])!
    var calculatedArr = [Int]()
    var answer = 0
    
    (0...9).forEach { calculatedArr.append( Int(pow(Float($0), Float(p))) )} // 각자리수의 p를 곱한 arr를 먼저 만든다. 0~9
    
//    print(calculatedArr)
    
    
    func calculator(num: String) -> String { // 각자리의 숫자를 P번곱한 값을 반환한다.
        var result: Int = 0
        num.forEach { char in
            let element = Int(String(char))!
            result += calculatedArr[element]
        }
        return String(result)
    }
    
    
    while true {
        let num = arr.last!
        let m = calculator(num: num)
        
        print(m)
        if arr.contains(m) {
            let index = arr.firstIndex(of: m)!
            arr.removeSubrange(Int(exactly: index)!...)
            break
        } else {
            arr.append(m)
        }
    }
    
    print(arr.count)
    
}
