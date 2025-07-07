import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image,TouchableHighlight} from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/image.jpg')} style={styles.image}/>
      <TouchableHighlight onPress={() => alert('Hello! How are you?')}>
        <Text style={styles.text}>Click me</Text>
      </TouchableHighlight> 
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },

  image: {
    width: 200,
    position: 'absolute',
    height: 200,
    alignItems: 'center',
    justifyContent: 'center',
  },

  text: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#6495ed',
    top: 60,
    left: 60,
    padding: 60
  },
});
