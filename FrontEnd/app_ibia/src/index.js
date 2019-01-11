import React, {Component} from 'react';
import {
    Dimensions
}from 'react-native';
import {StackNavigator} from 'react-navigation';
import CardStackStyleInterpolator from 'react-navigation/src/views/CardStackStyleInterpolator'
const {width, height} = Dimensions.get('window');
import StackViewStyleInterpolator from 'react-navigation-stack/dist/views/StackView/StackViewStyleInterpolator';

//views
import App from './app/carga.js';
import Login from './app/login/transicion.js';

//custom transition
export const fromToptoBotton = (index, position) => {
    const imputRage =[0, index, index + 0.80, index + 1] ;
    const opacity = position.interpolate({
        inputRage,
        outputRage: [1,1,1,1]
    })
    const translateY = position.interpolate({
        inputRage,
        outputRage: [height, 0, 0, 0]
    })


return {
    opacity,
    transform: [
        {translateY}
    ]
}
}
//transition config
const transConfig = () => {
    return {
        screenInterpolator: (sceneProps) => {
            const {position, scene} = sceneProps;
            const {index, route} = scene;
            const params = route.parans || {}
            const transition = parans.transition || 'default';

            return {
                //list of transitions
                default: CardStackStyleInterpolator.forHorizontal(sceneProps),
                fromToptoBotton: fromToptoBotton(index, position)
            }[transition]
        }
    }
}

//Scenes
let scenes = {
    Home: {
        screen: App
    },
    Login: {
        screen: Login
    }
}

const Stack = StackNavigator(scenes, {
        //transitions config
        transitionConfig: null
})
export default Stack;