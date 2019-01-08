import React, {Component} from 'react';
import { Alert,
Platform,
AppRegistry,
StyleSheet,
Text, 
View, 
TouchableOpacity,
TextInput,
Dimensions,
Image,
ScrollView,
WebView
} from 'react-native';

export default class Touchables extends Component {

constructor(props, env){
  super(props, env);

  this.state = {
    colorFondo: 'blue',
    direccion: 'http://google.com'
  }
}
    cambiarColor(){

    this.setState({colorFondo: this.state.text})
    }

    cambiarPagina(){
      this.setState({direccion: this.state.text})
    }

  render() {
    return (
      <ScrollView>
        <View style={{
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: this.state.colorFondo,
      }}>
          <Image
            style={{width: 500, height: 500}}
            source={{uri: 'https://www.rizog.com/wp-content/uploads/2017/02/Dise%C3%B1o-del-b%C3%BAho-dise%C3%B1os-para-mujeres-1.jpg'}}
          />
          <WebView
            source={{uri: this.state.direccion}}
            style={{width: Dimensions.get('window').width, height: 500, backgroundColor: 'white'}}
          />
        <TextInput
            style={{height: 40, borderColor: 'gray', borderWidth: 1, width: (Dimensions.get('window').width * 80 / 100),margin: 15,}}
            placeholder="Type here to translate!"
            onChangeText={(text) => this.setState({text})}
            value={this.state.text}
          />

          <TouchableOpacity style={styles.boton}  onPress={this.cambiarColor.bind(this)}>
          <Text style={styles.textoBoton}>cambiar pagina</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.boton}  onPress={this.cambiarColor.bind(this)}>
          <Text style={styles.textoBoton}>cambiar color</Text>
          </TouchableOpacity>
          </View>
       </ScrollView>
    );
  }
} 

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
boton: {
  backgroundColor: 'purple',
  width: 300,
  height: 50,
  borderWidth: 2,
  borderColor: 'black',
  borderRadius: 15,
  alignItems: 'center',
  flexDirection: 'row'

},
textoBoton:{
  color: 'white',
  fontSize: 20,
  textAlign: 'center',
  flex: 1
}
});
