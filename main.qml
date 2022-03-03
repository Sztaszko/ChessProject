import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.15

Window {
    id: mainWindow
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    GridLayout {
        id: mainGridView

        columns: 2
        rows: 3
        Text {
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            text: "Player 1"

        }
        Text {
            text: "Info"
        }

        Rectangle {
            id: board

            Layout.alignment: Qt.AlignCenter
            width: 2*mainWindow.width/3
            height: 2*mainWindow.width/3
            color: "transparent"
            Grid {

                columns: 8
                rows: 8
                Repeater {
                    model: 64
                    Rectangle {
                        function chess_pattern(ind) {
                            if (parseInt(ind/8, 10) %2 == 0)
                                return ind%2 == 0? "white" : "black"
                            else
                                return ind%2 == 0? "black" : "white"
                        }

                        width: board.width/8
                        height: board.height/8
                        border.color: "black"
                        color: chess_pattern(index)

                    }
                }
            }
        }

        Text {
            text: "Info"
        }

        Text {
            text: "Player 2"
        }
    }
}
