import React, {Component} from 'react';
import { 
StyleSheet,
Text, 
View, 
Dimensions,
Image
} from 'react-native';

export default class ImagenExterna extends Component {

constructor(props, env){
  super(props, env);

  this.state = {
    colorFondo: 'white',
  }
}

  render() {
    return (
     <View>
      <Image 
        style={{width: 200, height: 200}}
        source={{uri: this.props.urlImagen}}
        />
        <Text>
          {this.props.texto}
        </Text>
     </View>
    );
  }
} 

const styles = StyleSheet.create({
}
);
