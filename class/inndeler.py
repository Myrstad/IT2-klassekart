class Inndeler:
  def __init__(self, antall_grupper, gruppestørrelse) -> None:
    pass
  
  @staticmethod
  def hent_elever(fil_navn):
    with open(fil_navn, 'r', encoding='utf-8') as fil:
      tekst = fil.read()
      elever = tekst.split('\n')
      return elever

  def del_per_antall_grupper() -> list[str]:
    return ['hei']
  
  def del_per_gruppestørrelse() -> list[str]:
    return ['hei']
  
if __name__ == '__main__':
  i = Inndeler(None, None)
  print(i.hent_elever('elever.txt'))
  i.del_per_antall_grupper()

