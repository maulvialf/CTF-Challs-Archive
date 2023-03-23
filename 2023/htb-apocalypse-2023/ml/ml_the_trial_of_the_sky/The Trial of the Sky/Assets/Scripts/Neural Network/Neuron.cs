using System.Collections.Generic;
using System;

[Serializable]
public class Neuron
{
    
    public List<Dendrite> dendrites;
    public double bias;
    public double delta;
    public double value;

    public int NumDendrites(){
        return dendrites.Count;
    }

    public Neuron(){
        this.bias = UnityEngine.Random.Range(-1f, 1f);

        this.dendrites = new List<Dendrite>();
    }

    public Neuron(int bias){
        this.bias = bias;
        this.dendrites = new List<Dendrite>();
    }

}
