import Foundation

var janggoon: Int = 0
var byeongjeong: Int = 0
var ilban: Int = 0
func solution(_ hp:Int) -> Int {
    janggoon = hp / 5
    byeongjeong = (hp - (5*janggoon)) / 3
    ilban = (hp-(5*janggoon)-(3*byeongjeong)) / 1
    return janggoon + byeongjeong + ilban
}
