import React, {Component} from 'react';
import {
    Text,
    View,
    TocuhableHightlight,
    StyleSheet
} from 'react-native';

class Index extends Component {
    render(){
        return (
            <View style = {styles.container}>
                <Text>Carga App</Text>
                <TocuhableHightlight>
                <Text>Login with Custon transition</Text>
                </TocuhableHightlight>
                <TocuhableHightlight>
                <Text>Login with default transition</Text>
                </TocuhableHightlight>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1
    }

})

export default Index;