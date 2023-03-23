using UnityEngine;
using System.Collections.Generic;
using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

[Serializable]
public class NeuralNetwork
{
    public List<Layer> layers;
    public int[] layerStructure;
    public float fitness;
    public double fitnessRatio;

    public int NumLayers(){
        return layers.Count;

    }

    public NeuralNetwork(int[] layers){
        if (layers.Length < 2){
            return;
        }

        this.layers = new List<Layer>();
        this.layerStructure = layers;
        this.fitness = 0f;
        this.fitnessRatio = 0f;

       
        for (int i = 0; i < layers.Length; i++){
            
            Layer currentLayer = new Layer(layers[i], i);
            this.layers.Add(currentLayer);

           
            for (int n = 0; n < layers[i]; n++){
                currentLayer.neurons.Add(new Neuron());
            }

            
            foreach(Neuron neuron in currentLayer.neurons){
                
                if (i == 0){
                    neuron.bias = 0;
                }else{
                   
                    for (int d = 0; d < layers[i - 1]; d++){
                        neuron.dendrites.Add(new Dendrite());
                    }
                }
            }
        }
    }
    // Tests have shown that NNs with 6,5,2 layer structure will definetly work.
    public NeuralNetwork(String nn_info){
        nn_info = nn_info.Replace("\r", "");
        string[] lines = nn_info.Split("\n");
        Debug.Log(lines);
        string[] structure = lines[0].Split(new char[] { ',' });
        int[] numStrucutre = new int[structure.Length];
        for (int i = 0; i < structure.Length; i++){
            numStrucutre[i] = System.Convert.ToInt32(structure[i]);
        }

        
        NeuralNetwork NN = new NeuralNetwork(numStrucutre);

       
        string[] element = lines[1].Split(new char[] { ',' });

        List<Double> encoded = new List<double>();
        for (int i = 0; i < element.Length; i++){
            encoded.Add(Convert.ToDouble(element[i]));
            Debug.Log(encoded[i]);

        }

        
        NN.Decode(encoded);
        this.layers = NN.layers;
        this.layerStructure = NN.layerStructure;
        this.fitness = 0f;
        this.fitnessRatio = 0f;
    }

    
    public double Sigmoid(double x){
        return 1 / (1 + Math.Exp(-x));
    }
    double Tanh(double x){
        return System.Math.Tanh(x);
    }

    
    public List<double> Encode(){

        List<double> chromosome = new List<double>();
        
        for (int i = 1; i < layers.Count; i++){
            for (int j = 0; j < layers[i].neurons.Count; j++){
                
                chromosome.Add(layers[i].neurons[j].bias);
                
                for (int k = 0; k < layers[i].neurons[j].NumDendrites(); k++){
                    chromosome.Add(layers[i].neurons[j].dendrites[k].weight);
                }
            }
        }
        return chromosome;
    }

    
    public void Decode(List<double> chromosome){
        int geneIndex = 0;

        for (int i = 1; i < layers.Count; i++){
            for (int j = 0; j < layers[i].neurons.Count; j++){
                layers[i].neurons[j].bias = chromosome[geneIndex];
                geneIndex++;
                
                for (int k = 0; k < layers[i].neurons[j].NumDendrites(); k++){
                    layers[i].neurons[j].dendrites[k].weight = chromosome[geneIndex];
                    geneIndex++;
                }
            }
        }

    }

   
    public double[] Run(List<double> input){
       
        if (input.Count != this.layers[0].neurons.Count){
            return null;
        }

        
        for (int l = 0; l < layers.Count; l++){
            Layer currentLayer = layers[l];

            for (int n = 0; n < currentLayer.neurons.Count; n++){
                Neuron neuron = currentLayer.neurons[n];

                
                if (l == 0){
                    neuron.value = input[n];
                }else{ 
                   
                    neuron.value = 0;
                    for (int lastNeuron = 0; lastNeuron < this.layers[l - 1].neurons.Count; lastNeuron++){
                        neuron.value += this.layers[l - 1].neurons[lastNeuron].value * neuron.dendrites[lastNeuron].weight;
                    }

                   
                    if (l != layers.Count - 1){
                        neuron.value = Sigmoid(neuron.value + neuron.bias);
                    }
                    else{
                        neuron.value = Tanh(neuron.value + neuron.bias);
                    }
                } 
            }
        }

        
        Layer lastLayer = this.layers[this.layers.Count - 1];
        int numOutput = lastLayer.neurons.Count;
        double[] output = new double[numOutput];
        for (int i = 0; i < numOutput; i++){
            output[i] = lastLayer.neurons[i].value;
        }
        return output;
    }
    public void Save(){
        StreamWriter write = new StreamWriter("./nn" + (int)this.fitness + ".txt", true);

       
        for (int i = 0; i < layerStructure.Length-1; i++){
            write.Write(layerStructure[i] + ", ");
        }
        write.Write(layerStructure[layerStructure.Length - 1] + "\n");

        
        List<double> encoded = this.Encode();
        for (int i = 0; i < encoded.Count - 1; i++)
        {
            write.Write(encoded[i] + ", ");
        }
        write.Write(encoded[encoded.Count - 1]);

        write.Close();
    }

}

